from rest_framework import serializers
from .models import *
from products.serializer import *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductsSerializer()
    
    class Meta:
        model = CartItems
        fields = '__all__'