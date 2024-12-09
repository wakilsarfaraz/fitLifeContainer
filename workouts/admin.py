from django.contrib import admin
from .models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'youtube_url')
    search_fields = ('title', 'description', 'category')
    list_filter = ('category',)

admin.site.register(Workout, WorkoutAdmin)