from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FitnessClass, UserClass
from django.contrib import messages

def classes(request):
    classes = FitnessClass.objects.all()
    return render(request, 'classes.html', {'classes': classes})

def class_detail(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    return render(request, 'class_detail.html', {'fitness_class': fitness_class})

@login_required
def add_to_calendar(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    if request.method == 'POST':
        date = request.POST.get('date')
        UserClass.objects.create(user=request.user, fitness_class=fitness_class, date=date)
        messages.success(request, 'Class added to your calendar.')
        return redirect('my_classes')
    return render(request, 'add_to_calendar.html', {'fitness_class': fitness_class})

@login_required
def my_classes(request):
    user_classes = UserClass.objects.filter(user=request.user).order_by('date')
    return render(request, 'my_classes.html', {'user_classes': user_classes})