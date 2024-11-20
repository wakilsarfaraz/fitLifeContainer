from django.shortcuts import render
from .models import Workout

def workouts_view(request):
    workouts = Workout.objects.all()
    categories = Workout.objects.values_list('category', flat=True).distinct()

    for workout in workouts:
        workout.video_id = workout.get_video_id()
        print(f"URL: {workout.youtube_url}, Video ID: {workout.video_id}") 

    return render(request, 'workouts.html', {
        'workouts': workouts,
        'categories': categories
    })