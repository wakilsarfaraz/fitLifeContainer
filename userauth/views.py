from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from .forms import CustomUserCreationForm

class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirect to homepage after logout

class UserRegistrationView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('userauth:login')  # Redirect to login after successful registration

    def form_valid(self, form):
        messages.success(self.request, "Your account has been created successfully! You can now log in.")
        return super().form_valid(form)