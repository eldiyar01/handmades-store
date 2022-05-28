from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('all-products/', products, name='products'),
    path('product/<int:pk>/', product, name='product')
]
