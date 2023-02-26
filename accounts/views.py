from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.
def test(request):
    return HttpResponse("<h1> OK </h1>")

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"