from django.shortcuts import render

from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from pprint import pprint
from django.db import transaction

# Create your views here.


def hello_view(request):
    message = "Hello World Django"
    return render(request, 'firstapp/hello.html', {'message': message})



#
#
#
# ----------------------------------------------------------------
# data serialization view for data entries
# ----------------------------------------------------------------
#

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryCreateView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandListView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)


class BrandCreateView(APIView):
    def post(self, request):
        serializer = BrandSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnitListView(APIView):
    def get(self, request):
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)


class UnitCreateView(APIView):
    def post(self, request):
        serializer = UnitSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SupplierListView(APIView):

    def get(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)

class SupplierCreateView(APIView):

    def post(self, request):
        serializer = SupplierSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    


class ProductListView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductCreateView(APIView):
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class PurchaseListView(APIView):
    def get(self, request):
        purchases = Purchase.objects.all()
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)



    

class PurchaseCreateView(APIView):
    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        
        if serializer.is_valid():
            with transaction.atomic():
                purchase = serializer.save()

                purchase_order_products_data = request.data.get('purchase_order_product', [])
                for single_data in purchase_order_products_data:
                    product_id = single_data.get('product')
                    quantity = single_data.get('quantity')
                    sub_total = single_data.get('sub_total')
                    
                    # Update stock_quantity for the Product
                    product = Product.objects.get(pk=product_id)
                    product.stock_quantity += quantity
                    product.save()
                    
                    purchase_order_product = Purchase_order_product(
                        product_id=product_id,
                        quantity=quantity,
                        sub_total=product.price * quantity,
                        purchase=purchase
                    )
                    purchase_order_product.save()

                    
            response = {
                'success': True,
                'message': 'Purchase successfull'
            }

            return Response(response, status=status.HTTP_201_CREATED)
        else:   
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class PurchaseCreateView(APIView):
#     def post(self, request):
        
#         purchase_order_products = request.data.get('purchase_order_product', [])
        
#         purchase_serializer = PurchaseSerializer(data=request.data)
#         purchase_order_product_serializer = PurchaseOrderProductSerializer(data=purchase_order_products, many=True)
        
#         if purchase_serializer.is_valid() and purchase_order_product_serializer.is_valid():
#             purchase = purchase_serializer.save()
#             for single_data in purchase_order_product_serializer.validated_data:
#                 product_id = single_data.get('product').id
#                 quantity = single_data.get('quantity')
#                 product = Product.objects.get(pk=product_id)
#                 product.stock_quantity += quantity
#                 product.save()
#                 Purchase_order_product.objects.create(
#                     purchase=purchase,
#                     product=product,
#                     sub_total=product.price * quantity,  # Or any other calculation based on your requirements
#                     quantity=quantity,
#                 )
#             return Response(purchase_serializer.data, status=status.HTTP_201_CREATED)
        
#         errors = {}
#         if not purchase_serializer.is_valid():
#             errors['purchase'] = purchase_serializer.errors
#         if not purchase_order_product_serializer.is_valid():
#             errors['purchased_products'] = purchase_order_product_serializer.errors
        
#         return Response(errors, status=status.HTTP_400_BAD_REQUEST)