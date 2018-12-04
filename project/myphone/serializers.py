from rest_framework import serializers
from myphone.models import Produit
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('id', 'name', 'price', 'description')