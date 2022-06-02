from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('all-products/', products, name='products'),
    path('product/<int:pk>/', product, name='product'),
    path('buy/<int:pk>', buy, name='buy'),
    path('buy/shipping/', shipping, name='shipping'),
    path('categories/', categories, name='categories'),
    path('category/<int:pk>/products', category_p, name='category'),
    path('about-us/', about, name='about')
]
