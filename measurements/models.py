from djongo import models

class Measurement(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='measurements')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    chest = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hips = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    thighs = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    calves = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    left_arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    right_arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=10)
    notes = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)  # Allow users to set the date
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Add BMI field

    def to_dict(self):
        return {
            'id': str(self.pk),
            'user_id': str(self.user.pk),
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
            'date': self.date.isoformat() if self.date else None,
            'bmi': str(self.bmi) if self.bmi else None,  # Include BMI in dict
        }

    class Meta:
        db_table = 'measurements_measurement'