from django.shortcuts import render
from .models import *


def home(request):
    f_products = Product.objects.filter(featured=True)
    return render(request, 'home.html', {'products': f_products})


def products(request):
    pass