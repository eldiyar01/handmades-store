from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from .models import User


class SignUpForm(UserCreationForm):
    username = UsernameField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'phone_number')
