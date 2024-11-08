from django.db import models
from django.contrib.auth.models import User

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
    time = models.TimeField()
    image = models.ImageField(upload_to='class_images/')

    def __str__(self):
        return self.name

class UserClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'fitness_class', 'date')