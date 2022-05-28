from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from .models import User


class SignUpForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-0',
                                                               'placeholder': 'Your name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-0',
                                                              'placeholder': 'Your lastname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control rounded-0',
                                                            'placeholder': 'Email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-0',
                                                            'placeholder': 'Address to delivery'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-0',
                                                                 'placeholder': 'Your phone number (507004522)'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control rounded-0',
                                                                  'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control rounded-0',
                                                                  'placeholder': 'Password Again'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'phone_number')
