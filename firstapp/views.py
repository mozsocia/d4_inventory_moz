from django.shortcuts import render

# Create your views here.


def hello_view(request):
    message = "Hello World Django"
    return render(request, 'firstapp/hello.html', {'message': message})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Purchase, PurchasedProduct
from .serializers import PurchaseSerializer, PurchasedProductSerializer
from django.db import transaction

class PurchaseListCreateAPIView(APIView):
    def get(self, request):
        purchases = Purchase.objects.all()
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)

    def post(self, request):
        purchase_serializer = PurchaseSerializer(data=request.data)
        
        
        purchased_products_serializer = PurchasedProductSerializer(
            data=request.data.get('purchased_products'), many=True)
        
        if purchase_serializer.is_valid() and purchased_products_serializer.is_valid():
            # purchase = purchase_serializer.save()
            with transaction.atomic():
                purchase_data = purchase_serializer.validated_data
                purchase = Purchase.objects.create(
                    name=purchase_data['name'],
                    total_price=purchase_data['total_price']
                )
                
                for purchased_product_data in purchased_products_serializer.data:
                    product_id = purchased_product_data['product']
                    quantity = purchased_product_data['quantity']
                    
                    product = Product.objects.get(pk=product_id)
                    product.quantity += quantity
                    product.save()
                    
                    PurchasedProduct.objects.create(
                        purchase=purchase,
                        product=product,
                        quantity=quantity
                    )
                
            return Response(purchase_serializer.data, status=status.HTTP_201_CREATED)
        
        errors = {}
        if not purchase_serializer.is_valid():
            errors['purchase'] = purchase_serializer.errors
        if not purchased_products_serializer.is_valid():
            errors['purchased_products'] = purchased_products_serializer.errors
        
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)