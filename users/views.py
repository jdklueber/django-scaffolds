from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class SignUpPageView(generic.CreateView):
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')