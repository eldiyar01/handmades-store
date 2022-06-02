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


def buy(request, pk):
    user = request.user
    o_product = Product.objects.get(id=pk)
    return render(request, 'product/buy.html', {'product': o_product, 'user': user})


def shipping(request):
    if request.method == 'POST':
        msg = 'Thanks! soon admins will write to you for details'
        user = request.user
        form = request.POST
        product_n = form.get('p_title')
        amount = int(form.get('amount'))
        price = int(form.get('p_price'))
        shipping_a = user.address
        Sells.objects.create(product_n=product_n, amount=amount, total_p=amount*price,
                             shipping_a=shipping_a, client_n=user, client_p=user.phone_number)
    else:
        return reverse('product:products')
    return render(request, 'product/success.html', {'msg':msg})


def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'product/categories.html', {'categories': all_categories})


def category_p(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, 'product/c_products.html', {'category': category})


def about(request):
    return render(request, 'product/about.html')