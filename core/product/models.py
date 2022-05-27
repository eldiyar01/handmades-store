from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=255, blank=True)


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)


class Gallery(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_img', blank=True)
