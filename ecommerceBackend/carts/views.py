from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *

class CartView(APIView):

    def get(self, request):
        queyset = CartItems.objects.all()
        return Response({'data': 'OK'},status=status.HTTP_200_OK)
    
    def post(self, request):
        pass

    def update(self, request):
        pass

    def delete(self, request):
        pass

