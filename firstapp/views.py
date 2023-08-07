from django.shortcuts import render
from django.views import View
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

def test_view(request):
    return render(request, 'firstapp/test.html')



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
    def get(self, request):
        return render(request, 'firstapp/purchase/create_purchase.html')
    
    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        
        if serializer.is_valid():
            
            purchase_data = serializer.validated_data
            purchase_order_products_data = purchase_data.pop('purchase_order_product')
            pprint(purchase_order_products_data)
            
            with transaction.atomic():
                purchase = Purchase.objects.create(**purchase_data)

                for single_data in purchase_order_products_data:
                    product_id = single_data.get('product').id
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
        
        



#
# --- Sales ----------------------------------------------------------------
#
class SaleListView(View):
    def get(self, request):
        sales = Sale.objects.all()
        return render(request, 'sales/sale_list.html', {'sales': sales})


class CreateSaleView(View):
    def get(self, request):
        # form = SaleForm()
        return render(request, 'firstapp/sales/create_sale.html')

    # def post(self, request):
    #     form = SaleForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('sale_list')
    #     return render(request, 'sales/create_sale.html', {'form': form})

class SaleListAPIView(APIView):
    def get(self, request):
        sales = Sale.objects.all()
        # Add any filtering, sorting, or pagination here if needed
        serializer = SaleGetSerializer(sales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

class SaleCreateAPIView(APIView):
    def get(self, request):
        return render(request, 'firstapp/sales/create_sale.html')
    
    def post(self, request):
        serializer = SaleCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            with transaction.atomic():
                
                try:
                    
                    sale_data = serializer.validated_data
                    sale_order_products_data = sale_data.pop('sale_order_product')
                    
                    # Set total_quantity and total to zero initially
                    sale_data['total_quantity'] = 0
                    sale_data['total'] = 0.0

                    # Create Sale object
                    sale = Sale.objects.create(**sale_data)

                    for product_data in sale_order_products_data:
               
                        quantity = product_data['quantity']
            
                        product = product_data['product']
                        sub_total = product.price * quantity

                        # Create Sale_order_product object with the created Sale object as the reference
                        Sale_order_product.objects.create(sale=sale, product=product, quantity=quantity, sub_total=sub_total)

                        # Update total_quantity and total as we iterate through Sale_order_product instances
                        sale.total_quantity += quantity
                        sale.total += sub_total

                        # Decrement the Product stock_quantity by the sale quantity
                        product.stock_quantity -= quantity
                        product.save()

                    # Save the updated Sale object
                    sale.save()
                    
                except Exception as e:
                    # Handle any other unexpected errors here
                    pprint(e)
                    return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
                response = {
                    'success': True,
                    'message': 'Sale create successfull'
                }
            return Response(response, status=status.HTTP_201_CREATED)
        pprint(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)



class CustomerCreateView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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