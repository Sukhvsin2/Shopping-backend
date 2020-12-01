from rest_framework import serializers
from .models import Category, Product, QuantityVariant, ColorVariant, SizeVariant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    # This is for the particular data like category id = 1 but after this we get category like vegetables
    category = CategorySerializer()
    quantity_type = QuantitySerializer()
    color_type = ColorSerializer()
    size_type = SizeSerializer()
    class Meta:
        model = Product
        fields = '__all__'

