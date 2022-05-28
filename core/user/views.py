from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .forms import SignUpForm, SignInForm
from .models import User


def profile(request):
    return render(request, 'user/profile.html')


class SignUp(CreateView):
    template_name = 'user/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('product:home')

    def get_queryset(self):
        return User.objects.all()


class SignIn(LoginView):
    form_class = SignInForm
    template_name = 'user/signin.html'


class SignOut(LogoutView):
    template_name = 'user/login.html'


