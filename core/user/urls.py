from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', SignUp.as_view(), name='signup'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
]
