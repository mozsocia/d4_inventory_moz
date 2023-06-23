from django.urls import path
from .views import *


urlpatterns = [
    path('hello/', hello_view, name='hello'),
    
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('purchases/', PurchaseListCreateAPIView.as_view(), name='purchase-list-create'),
]