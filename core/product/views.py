from django.shortcuts import render
from .models import *
from user.models import User


def home(request):
    f_products = Product.objects.filter(featured=True)
    return render(request, 'home.html', {'f_products': f_products})


def products(request):
    all_products = Product.objects.all()
    return render(request, 'product/products.html', {'products': all_products})


def product(request, pk):
    o_product = Product.objects.get(id=pk)
    return render(request, 'product/product.html', {'product': o_product})


def buy(request, pk):
    user = User.objects.get(id=request.user.id)
    o_product = Product.objects.get(id=pk)
    return render(request, 'product/buy.html', {'product': o_product, 'user': user})


def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'product/categories.html', {'categories': all_categories})


def category_p(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, 'product/c_products.html', {'category': category})


def about(request):
    return render(request, 'product/about.html')