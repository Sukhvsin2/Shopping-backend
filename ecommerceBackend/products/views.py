from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializer import ProductsSerializer, CategorySerializer
from rest_framework import generics


class ProductsView(APIView):
    
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)