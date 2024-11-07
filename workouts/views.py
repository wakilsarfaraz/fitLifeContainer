from django.shortcuts import render

# Create your views here.
def workouts_view(request):
    return render(request,"workouts.html")
