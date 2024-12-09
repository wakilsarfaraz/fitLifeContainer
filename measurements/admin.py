from django.contrib import admin
from .models import Measurement

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height', 'chest', 'waist', 'hips', 'thighs', 'calves', 'left_arm', 'right_arm', 'unit', 'date', 'bmi')
    list_filter = ('user', 'date')
    search_fields = ('user__username',)  # Allow searching by username
    ordering = ('-date',)  # Order by date descending

admin.site.register(Measurement, MeasurementAdmin)