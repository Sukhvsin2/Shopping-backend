from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializer import ProductsSerializer, CategorySerializer
from rest_framework import generics
# permissions
from rest_framework.permissions import IsAuthenticated


class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'success': 'LoggedIn successfully'}, status=status.HTTP_200_OK)

class ProductsView(APIView):
    
    def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__category_name= category)
        else:
            queryset = Product.objects.all()
        serializer = ProductsSerializer(queryset, many=True)

        context = {
            'total_count': len(serializer.data),
            'data': serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)
