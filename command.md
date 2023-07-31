py manage.py makemigrations firstapp

py manage.py migrate

py manage.py seed_db

py manage.py runserver




"""

class PurchaseCreateView(APIView):
    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        
        if serializer.is_valid():
            
            purchase_data = serializer.validated_data
            purchase_order_products_data = purchase_data.pop('purchase_order_product')
            
            with transaction.atomic():
                purchase = Purchase.objects.create(sale_data = serializer.validated_data)

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

"""
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