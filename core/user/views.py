from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from .models import User


class SignUp(CreateView):
    template_name = 'user/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('product:home')

    def get_queryset(self):
        return User.objects.all()

