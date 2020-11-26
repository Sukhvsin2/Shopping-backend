from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class FrontPage(APIView):

    def get(self, request):
        return Response(data={'data':"This is frontpage API."},status=status.HTTP_200_OK)