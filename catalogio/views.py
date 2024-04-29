from django.shortcuts import render

from rest_framework import generics

from .models import Product
from .serializer import ProductSerializer

'''
    Product CRUD
'''
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    permission_classes = []

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    permission_classes = []
    lookup_field = "pk"
