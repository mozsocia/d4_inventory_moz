from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        

class PurchaseOrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_order_product
        fields = '__all__'
        extra_kwargs = {
            'purchase': {'required': False}
        }

class PurchaseSerializer(serializers.ModelSerializer):
    purchase_order_product = PurchaseOrderProductSerializer(many=True)

    class Meta:
        model = Purchase
        fields = '__all__'