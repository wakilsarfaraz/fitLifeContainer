from django.db import models
from django.contrib.auth.models import User
import os
from django.contrib import admin

class FitnessClassAdmin(admin.ModelAdmin):
    exclude = ['id']

class UserClassAdmin(admin.ModelAdmin):
    exclude = ['id']

# Image upload path function
def fitness_class_image_upload_to(instance, filename):
    return os.path.join('classes', filename)

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    time = models.TimeField(null=True, blank=True)
    image = models.ImageField(upload_to=fitness_class_image_upload_to)
    location = models.CharField(max_length=100)  # New field for class location
    capacity = models.PositiveIntegerField(default=30)  # New field for class capacity

    def __str__(self):
        return self.name

class UserClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'fitness_class', 'date'], name='unique_user_class_date')
        ]