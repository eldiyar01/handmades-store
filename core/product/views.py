from django.shortcuts import render
from .models import *


def home(request):
    f_products = Product.objects.filter(featured=True)
    return render(request, 'home.html', {'f_products': f_products})


def products(request):
    all_products = Product.objects.all()
    return render(request, 'product/products.html', {'products': all_products})


def product(request, pk):
    o_product = Product.objects.get(id=pk)
    return render(request, 'product/product.html', {'product': o_product})
