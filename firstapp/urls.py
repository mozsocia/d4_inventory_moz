from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    
    
        # serializers urls for data entries

    path('api_d/categories/', CategoryListView.as_view(), name='category-list'),
    path('api_d/categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('api_d/brands/', BrandListView.as_view(), name='brand-list'),
    path('api_d/brands/create/', BrandCreateView.as_view(), name='brand-create'),
    path('api_d/units/', UnitListView.as_view(), name='unit-list'),
    path('api_d/units/create/', UnitCreateView.as_view(), name='unit-create'),
    
    path('api_d/suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('api_d/suppliers/create/', SupplierCreateView.as_view(), name='supplier-create'),
    
    path('api_d/products/', ProductListView.as_view(), name='product-list'),
    path('api_d/products/create/', ProductCreateView.as_view(), name='product-create'),
    
    path('api_d/purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('api_d/purchases/create/', PurchaseCreateView.as_view(), name='purchase-create'),



]
