from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect

from .forms import *
from .models import User


def profile(request):
    return render(request, 'user/profile.html')


@login_required
def change(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            print(img_obj)
            return render(request, 'user/profile.html', {'img_obj': img_obj })
    else:
        form = ChangeForm(instance=request.user)

    return render(request, 'user/change.html', {'form': form })


class Change(PermissionRequiredMixin, UpdateView):
    permission_required = ("is_staff",)
    model = User
    form_class = ChangeForm
    template_name = 'user/change.html'

    def get_queryset(self):
        return self.model.objects.filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse('user:profile')


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


