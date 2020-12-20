from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .seralizer import *

class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response({'total': len(serializer.data),'data':serializer.data},status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        user = request.user
        cart,_ = Cart.objects.get_or_create(user=user, ordered=False)
        product = Product.objects.get(id=data.get('product'))
        price = product.product_price
        quantity = data.get('quantity')
        cart_items = CartItems(user=user, product=product, cart=cart, price=price, quantity=quantity)
        cart_items.save()

        total_price = 0
        cart_items = CartItems.objects.filter(user=user, cart=cart.id)
        for item in cart_items:
            total_price += item.price
        cart.total_price = total_price
        cart.save()
        return Response({'data': 'Item Added!'},status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        cart_item = CartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'Items Updated!'}, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        data = request.data

        cart_item = CartItems.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Orders.objects.filter(user=request.user)
        serializer = OrderSerializer(queryset, many=True)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_404_NOT_FOUND)