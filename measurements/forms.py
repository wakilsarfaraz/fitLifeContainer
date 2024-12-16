from django import forms
from decimal import Decimal, InvalidOperation
from .models import Measurement
from django.core.exceptions import ValidationError

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'weight', 'height', 'chest', 'waist', 'hips',
            'thighs', 'calves', 'left_arm', 'right_arm', 'unit', 'notes', 'date'
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        return self.validate_measurement(weight, "Weight")

    def clean_height(self):
        height = self.cleaned_data.get('height')
        return self.validate_measurement(height, "Height")

    def clean_chest(self):
        chest = self.cleaned_data.get('chest')
        return self.validate_measurement(chest, "Chest measurement")

    def clean_waist(self):
        waist = self.cleaned_data.get('waist')
        return self.validate_measurement(waist, "Waist measurement")

    def clean_hips(self):
        hips = self.cleaned_data.get('hips')
        return self.validate_measurement(hips, "Hips measurement")

    def clean_thighs(self):
        thighs = self.cleaned_data.get('thighs')
        return self.validate_measurement(thighs, "Thighs measurement")

    def clean_calves(self):
        calves = self.cleaned_data.get('calves')
        return self.validate_measurement(calves, "Calves measurement")

    def clean_left_arm(self):
        left_arm = self.cleaned_data.get('left_arm')
        return self.validate_measurement(left_arm, "Left arm measurement")

    def clean_right_arm(self):
        right_arm = self.cleaned_data.get('right_arm')
        return self.validate_measurement(right_arm, "Right arm measurement")

    def validate_measurement(self, value, field_name):
        if value is not None:
            try:
                # Convert to Decimal safely
                value = Decimal(str(value))
            except InvalidOperation:
                raise ValidationError(f"{field_name} must be a valid number.")
            
            if value < 0 or value > 999.99:
                raise ValidationError(f"{field_name} must be between 0 and 999.99.")
            
            # Round to 2 decimal places
            value = round(value, 2)

        return value

    def clean_unit(self):
        unit = self.cleaned_data.get('unit')
        if unit and len(unit) > 10:
            raise ValidationError("Unit cannot exceed 10 characters.")
        return unit

    def clean_notes(self):
        notes = self.cleaned_data.get('notes')
        if notes and len(notes) > 500:
            raise ValidationError("Notes cannot exceed 500 characters.")
        return notes