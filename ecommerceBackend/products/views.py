from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .import models
from .serializer import ProductsSerializer, CategorySerializer
from rest_framework import generics


class ProductsView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductsSerializer

    # def get(self, request, *args, **kwargs):
    #     queryset = models.Product.objects.all()
    #     serializer = ProductsSerializer(queryset)
    #     return Response(serializer.data, status=status.HTTP_200_OK)