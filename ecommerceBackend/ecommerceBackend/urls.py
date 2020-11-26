from django.contrib import admin
from django.urls import path, include
from . import views
from products import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FrontPage.as_view(), name='FrontPage'),
    path('products/', include(urls)),
]
