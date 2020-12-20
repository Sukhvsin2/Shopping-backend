from django.urls import path
from .views import *

urlpatterns = [
    path('', CartView.as_view(), name='CartItemView'),
    path('order', OrderAPI.as_view(), name='OrderApi')
]
