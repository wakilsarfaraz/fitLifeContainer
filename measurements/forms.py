from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'weight', 'height', 'chest', 'waist', 'hips', 
            'thighs', 'calves', 'left_arm', 'right_arm', 'unit', 'notes'
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
