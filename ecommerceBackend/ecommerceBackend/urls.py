from django.contrib import admin
from django.urls import path, include
from . import views
from products import urls as productUrls
from accounts import urls as accountUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FrontPage.as_view(), name='FrontPage'),
    path('api/products/', include(productUrls)),
    path('api/accounts/', include(accountUrls)),
]
