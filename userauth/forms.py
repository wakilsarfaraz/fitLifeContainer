import logging
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

logger = logging.getLogger(__name__)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        logger.debug(f"Checking if email {email} exists")
        
        # Fetch the user instead of using exists()
        user = User.objects.filter(email=email).first()
        if user:
            logger.error(f"Email {email} already exists.")
            raise forms.ValidationError("This email address is already in use.")
        
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        logger.debug(f"Checking if username {username} exists")
        
        # Fetch the user instead of using exists()
        user = User.objects.filter(username=username).first()
        if user:
            logger.error(f"Username {username} already exists.")
            raise forms.ValidationError("This username is already taken.")
        
        return username