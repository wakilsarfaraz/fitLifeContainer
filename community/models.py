from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=1000, default='Default Subject')  # Provide a default value
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def get_absolute_url(self):
        return reverse('community')
