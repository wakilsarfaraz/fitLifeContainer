from django.urls import path
from .views import UserRegistrationView, CustomLogoutView

app_name = 'userauth'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('login/', CustomLogoutView.as_view(), name='login'),
]