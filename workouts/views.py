from django.shortcuts import render
from .models import Workout

def workouts_view(request):
    workouts = Workout.objects.all()
    categories = Workout.objects.values_list('category', flat=True).distinct()
    return render(request, 'workouts.html', {'workouts': workouts, 'categories': categories})