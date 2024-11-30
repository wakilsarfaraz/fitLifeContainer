from djongo import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Measurement(models.Model):
    UNIT_CHOICES = [
        ('cm', 'Centimeters'),
        ('in', 'Inches'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='measurements')
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.01)])
    height = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.01)])
    chest = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0.01)])
    waist = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0.01)])
    hips = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0.01)])
    thighs = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0.01)])
    calves = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0.01)])
    left_arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0.01)])
    right_arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0.01)])
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='cm')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Measurement by {self.user.username} on {self.date}"

    def to_dict(self):
        return {
            'id': self.id,
            'weight': str(self.weight),
            'height': str(self.height),
            'chest': str(self.chest) if self.chest else None,
            'waist': str(self.waist) if self.waist else None,
            'hips': str(self.hips) if self.hips else None,
            'thighs': str(self.thighs) if self.thighs else None,
            'calves': str(self.calves) if self.calves else None,
            'left_arm': str(self.left_arm) if self.left_arm else None,
            'right_arm': str(self.right_arm) if self.right_arm else None,
            'unit': self.unit,
            'notes': self.notes,
            'date': self.date.isoformat(),  # Format date for JSON
        }

    class Meta:
        ordering = ['-date']