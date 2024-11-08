from django.shortcuts import render
from .models import Workout

def workouts_view(request):
    workouts = Workout.objects.all()
    categories = Workout.objects.values_list('category', flat=True).distinct()

    # Add the YouTube video ID to each workout object for easy access in the template
    for workout in workouts:
        workout.video_id = workout.get_video_id()

    return render(request, 'workouts.html', {
        'workouts': workouts,
        'categories': categories
    })
