from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    
    
        # serializers urls for data entries

    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('api/brands/', BrandListView.as_view(), name='brand-list'),
    path('api/brands/create/', BrandCreateView.as_view(), name='brand-create'),
    path('api/units/', UnitListView.as_view(), name='unit-list'),
    path('api/units/create/', UnitCreateView.as_view(), name='unit-create'),
    
    path('api/suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('api/suppliers/create/', SupplierCreateView.as_view(), name='supplier-create'),
    
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/create/', ProductCreateView.as_view(), name='product-create'),
    
    path('api/purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('api/purchases/create/', PurchaseCreateView.as_view(), name='purchase-create'),


    path('api/customers/', CustomerListView.as_view(), name='customer-list'),
    path('api/customers/create/', CustomerCreateView.as_view(), name='customer-create'),


    path('sales/create/', CreateSaleView.as_view(), name='create_sale'),
    
    path('api/sales/', SaleListAPIView.as_view(), name='sale-list'),
    path('api/sales/create/', SaleCreateAPIView.as_view(), name='sale-create'),


]
