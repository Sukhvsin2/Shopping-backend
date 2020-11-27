from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name='ProductView'),
    path('demo/', views.DemoView.as_view(), name='DemoView')
]
