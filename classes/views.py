from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FitnessClass, UserClass

def classes_view(request):
    classes = FitnessClass.objects.all()
    return render(request, 'classes.html', {'classes': classes})

@login_required
def add_to_my_classes(request, class_id):
    fitness_class = FitnessClass.objects.get(id=class_id)
    UserClass.objects.get_or_create(user=request.user, fitness_class=fitness_class)
    return redirect('classes:classes')

@login_required
def my_classes(request):
    user_classes = UserClass.objects.filter(user=request.user)
    return render(request, 'my_classes.html', {'user_classes': user_classes})