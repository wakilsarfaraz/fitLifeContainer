from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class UserRegistrationView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('userauth:login')  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = '/'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')