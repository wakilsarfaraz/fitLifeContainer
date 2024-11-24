from django.shortcuts import render, redirect, get_object_or_404
from .models import Measurement
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def measurement_list(request):
    if request.user.is_authenticated:
        measurements = request.user.measurements.all()
    else:
        measurements = []  # No measurements for anonymous users
    return render(request, 'measurement_list.html', {'measurements': measurements})

@csrf_exempt  # Use with caution
def add_measurement(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'success': False, 'error': 'User not authenticated'}, status=403)
        
        data = json.loads(request.body)
        measurement = Measurement.objects.create(
            user=request.user,
            weight=data.get('weight'),
            height=data.get('height'),
            chest=data.get('chest'),
            waist=data.get('waist'),
            hips=data.get('hips'),
            thighs=data.get('thighs'),
            calves=data.get('calves'),
            left_arm=data.get('left_arm'),
            right_arm=data.get('right_arm'),
            unit=data.get('unit'),
            notes=data.get('notes'),
        )
        return JsonResponse({'success': True, 'measurement': measurement.to_dict()})
    
    return JsonResponse({'success': False}, status=400)

@csrf_exempt  # Use with caution
def edit_measurement(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk)
    
    if request.method == 'POST':
        if measurement.user != request.user:
            return JsonResponse({'success': False, 'error': 'Not authorized'}, status=403)
        
        data = json.loads(request.body)
        measurement.weight = data.get('weight')
        measurement.height = data.get('height')
        measurement.chest = data.get('chest')
        measurement.waist = data.get('waist')
        measurement.hips = data.get('hips')
        measurement.thighs = data.get('thighs')
        measurement.calves = data.get('calves')
        measurement.left_arm = data.get('left_arm')
        measurement.right_arm = data.get('right_arm')
        measurement.unit = data.get('unit')
        measurement.notes = data.get('notes')
        measurement.save()
        return JsonResponse({'success': True, 'measurement': measurement.to_dict()})

    return JsonResponse({'success': False}, status=400)

@csrf_exempt  # Use with caution
def delete_measurement(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk)
    
    if measurement.user != request.user:
        return JsonResponse({'success': False, 'error': 'Not authorized'}, status=403)

    measurement.delete()
    return JsonResponse({'success': True})