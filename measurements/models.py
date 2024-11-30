from djongo import models

class Measurement(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='measurements')  # Added related_name
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    chest = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    hips = models.DecimalField(max_digits=5, decimal_places=2)
    thighs = models.DecimalField(max_digits=5, decimal_places=2)
    calves = models.DecimalField(max_digits=5, decimal_places=2)
    left_arm = models.DecimalField(max_digits=5, decimal_places=2)
    right_arm = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=10)
    notes = models.TextField(blank=True)

    def to_dict(self):
        return {
            'id': str(self.pk),
            'user_id': str(self.user.pk),
            'weight': str(self.weight),
            'height': str(self.height),
            'chest': str(self.chest),
            'waist': str(self.waist),
            'hips': str(self.hips),
            'thighs': str(self.thighs),
            'calves': str(self.calves),
            'left_arm': str(self.left_arm),
            'right_arm': str(self.right_arm),
            'unit': self.unit,
            'notes': self.notes,
        }

    class Meta:
        db_table = 'measurements_measurement'
