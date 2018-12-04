from django.shortcuts import render

from myphone.models import Produit
from myphone.serializers import ProductSerializer
from rest_framework import generics
    
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProductSerializer