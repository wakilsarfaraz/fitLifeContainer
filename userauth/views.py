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
    
    # This method is called when the login form is valid
    def form_valid(self, form):
        user = form.get_user()  # Get the logged-in user

        if user.is_staff:  # Check if the user is an admin
            return redirect('/admin/')  # Redirect admins to the admin page

        # If the user is not an admin, redirect to the success_url
        return super().form_valid(form)  # Redirect to the default success_url

    # Set the success_url for non-admin users (the default success page)
    success_url = reverse_lazy('home')