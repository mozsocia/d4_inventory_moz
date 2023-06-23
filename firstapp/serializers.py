# serializers.py
from rest_framework import serializers
from .models import Product, Purchase, PurchasedProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class PurchasedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedProduct
        fields = '__all__'
        extra_kwargs = {
            'purchase': {'required': False, "allow_null": True}
        }

