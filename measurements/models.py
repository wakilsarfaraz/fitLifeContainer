from django.db import models
from django.contrib.auth.models import User

class Measurement(models.Model):
    UNIT_CHOICES = [
        ('cm', 'Centimeters'),
        ('in', 'Inches'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='measurements')
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2) 
    height = models.DecimalField(max_digits=5, decimal_places=2)
    chest = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    hips = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  
    thighs = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    calves = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    left_arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    right_arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='cm')  
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Measurement by {self.user.username} on {self.date}"

    @property
    def bmi(self):
        if self.weight and self.height:
            # Convert height to meters if it's in centimeters, else in inches
            if self.unit == 'cm':
                height_in_meters = self.height / 100  # cm to meters
            else:
                height_in_meters = (self.height * 2.54) / 100  # inches to meters

            # Calculate BMI (weight in kg / height in meters squared)
            return round(self.weight / (height_in_meters ** 2), 2)
        return None

    class Meta:
        ordering = ['-date']
