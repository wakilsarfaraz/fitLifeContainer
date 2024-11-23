from django.urls import path
from .views import UserRegistrationView, CustomLogoutView, CustomLoginView  # Import your login view

app_name = 'userauth'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'), 
]