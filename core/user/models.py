from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=255, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=9, blank=True, unique=True)  # validators should be a list
    avatar = models.ImageField(upload_to='user_imgs', blank=True, null=True)
    purchases = models.IntegerField(default=0)