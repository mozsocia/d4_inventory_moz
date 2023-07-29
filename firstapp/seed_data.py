import random
import string
from django.utils import timezone
from .models import *
from .serializers import *

def generate_random_string(length):
    """Helper function to generate a random string of specified length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def load_data():
    
    data = [
        {
            "category_name": "Electronics",
            "parent": "Electronics & Appliances"
        },
        {
            "category_name": "Home Appliances",
            "parent": "Electronics & Appliances"
        }
    ]
    
    serializer = CategorySerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        
        
    data = [
        {
            "name": "Samsung",
            "discription": "Electronics brand"
        },
        {
            "name": "LG",
            "discription": "Electronics brand"
        }
    ]
    
    serializer = BrandSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        
        
    data = [
        {
        "name": "Piece"
        },
        {
            "name": "Kilogram"
        }
    ]
    
    serializer = UnitSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        
        
    data = [
        {
            "name": "Supplier 1",
            "supplier_type": "Type 1",
            "supplier_ID": "SUPP001",
            "address": "Address 1",
            "phone": 1234567890,
            "email": "supplier1@example.com",
            "start_date": "2023-07-27",
            "amount": 1000.50,
            "guarantor_name": "Guarantor 1",
            "guarantor_phone": 9876543210,
            "Created_at": "2023-07-27T12:34:56",
            "Updated_at": "2023-07-27T12:34:56"
        },
        {
            "name": "Supplier 2",
            "supplier_type": "Type 2",
            "supplier_ID": "SUPP002",
            "address": "Address 2",
            "phone": 9876543210,
            "email": "supplier2@example.com",
            "start_date": "2023-07-28",
            "amount": 2000.75,
            "guarantor_name": "Guarantor 2",
            "guarantor_phone": 1234567890,
            "Created_at": "2023-07-28T12:34:56",
            "Updated_at": "2023-07-28T12:34:56"
        }
        ]

    
    serializer = SupplierSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        
        
        
    
    data = [
        {
            "product_name": "Product 1",
            "product_code": "P1",
            "slug": "product-1",
            "price": 50,
            "discount_price": 40,
            "product_purchase_price": 30,
            "sort_discription": "Short description for Product 1",
            "discription": "Full description for Product 1",
            "stock_quantity": 0,
            "show_status": True,
            "meta_title": "Meta Title 1",
            "meta_keyword": "Keyword 1",
            "brand": 1, 
            "categoris": 1,  
            "unit": 1  
        },
        {
            "product_name": "Product 2",
            "product_code": "P2",
            "slug": "product-2",
            "price": 60,
            "discount_price": 50,
            "product_purchase_price": 35,
            "sort_discription": "Short description for Product 2",
            "discription": "Full description for Product 2",
            "stock_quantity": 0,
            "show_status": True,
            "meta_title": "Meta Title 2",
            "meta_keyword": "Keyword 2",
            "brand": 2,  
            "categoris": 1,  
            "unit": 2         
            }
        
        ]

    
    serializer = ProductSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()      
        
    print("Seeding successfull =================================")