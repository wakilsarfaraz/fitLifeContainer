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
        if weight is not None and (weight < 0 or weight > 999.99):
            raise ValidationError("Weight must be between 0 and 999.99.")
        if weight is not None:
            # Round to 2 decimal places
            weight = round(Decimal(weight), 2)
        return weight

    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height is not None and (height < 0 or height > 999.99):
            raise ValidationError("Height must be between 0 and 999.99.")
        if height is not None:
            # Round to 2 decimal places
            height = round(Decimal(height), 2)
        return height

    def clean_chest(self):
        chest = self.cleaned_data.get('chest')
        if chest is not None and (chest < 0 or chest > 999.99):
            raise ValidationError("Chest measurement must be between 0 and 999.99.")
        if chest is not None:
            # Round to 2 decimal places
            chest = round(Decimal(chest), 2)
        return chest

    def clean_waist(self):
        waist = self.cleaned_data.get('waist')
        if waist is not None and (waist < 0 or waist > 999.99):
            raise ValidationError("Waist measurement must be between 0 and 999.99.")
        if waist is not None:
            # Round to 2 decimal places
            waist = round(Decimal(waist), 2)
        return waist

    def clean_hips(self):
        hips = self.cleaned_data.get('hips')
        if hips is not None and (hips < 0 or hips > 999.99):
            raise ValidationError("Hips measurement must be between 0 and 999.99.")
        if hips is not None:
            # Round to 2 decimal places
            hips = round(Decimal(hips), 2)
        return hips

    def clean_thighs(self):
        thighs = self.cleaned_data.get('thighs')
        if thighs is not None and (thighs < 0 or thighs > 999.99):
            raise ValidationError("Thighs measurement must be between 0 and 999.99.")
        if thighs is not None:
            # Round to 2 decimal places
            thighs = round(Decimal(thighs), 2)
        return thighs

    def clean_calves(self):
        calves = self.cleaned_data.get('calves')
        if calves is not None and (calves < 0 or calves > 999.99):
            raise ValidationError("Calves measurement must be between 0 and 999.99.")
        if calves is not None:
            # Round to 2 decimal places
            calves = round(Decimal(calves), 2)
        return calves

    def clean_left_arm(self):
        left_arm = self.cleaned_data.get('left_arm')
        if left_arm is not None and (left_arm < 0 or left_arm > 999.99):
            raise ValidationError("Left arm measurement must be between 0 and 999.99.")
        if left_arm is not None:
            # Round to 2 decimal places
            left_arm = round(Decimal(left_arm), 2)
        return left_arm

    def clean_right_arm(self):
        right_arm = self.cleaned_data.get('right_arm')
        if right_arm is not None and (right_arm < 0 or right_arm > 999.99):
            raise ValidationError("Right arm measurement must be between 0 and 999.99.")
        if right_arm is not None:
            # Round to 2 decimal places
            right_arm = round(Decimal(right_arm), 2)
        return right_arm

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
