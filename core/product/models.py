from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('product:category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('product:product', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Gallery(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_img', blank=True)

    def __str__(self):
        return self.product.title


class Sells(models.Model):
    product_n = models.CharField(max_length=100, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    total_p = models.IntegerField(null=False, blank=False)
    shipping_a = models.CharField(max_length=100, blank=False)
    client_n = models.CharField(max_length=100, blank=False)
    client_p = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.product_n + ' ' +self.client_n