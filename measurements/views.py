# views.py
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_protect
from .models import Measurement
from .forms import MeasurementForm  
import json
from django.utils import timezone

def calculate_bmi(weight, height):
    if height > 0:
        return round(weight / ((height / 100) ** 2), 2)  # BMI = weight(kg) / height(m)^2
    return None

@login_required
def measurement_list(request):
    measurements = request.user.measurements.all()
    current_date = timezone.now().date()
    formatted_date = current_date.isoformat()
    return render(request, 'measurement_list.html', {'measurements': measurements, 'current_date': formatted_date})

@csrf_protect
@login_required
def add_measurement(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = MeasurementForm(data)

        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user
            measurement.bmi = calculate_bmi(measurement.weight, measurement.height)  # Calculate BMI
            measurement.save()
            return JsonResponse({'success': True, 'measurement': measurement.to_dict()}, status=201)
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    return JsonResponse({'success': False}, status=400)

@csrf_protect
@login_required
def edit_measurement(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk)
    if measurement.user != request.user:
        return JsonResponse({'success': False, 'error': 'Not authorized'}, status=403)

    if request.method == 'POST':
        data = json.loads(request.body)
        form = MeasurementForm(data, instance=measurement)

        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.bmi = calculate_bmi(measurement.weight, measurement.height)  # Calculate BMI
            measurement.save()
            return JsonResponse({'success': True, 'measurement': measurement.to_dict()})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    return JsonResponse({'success': False}, status=400)

class DeleteMeasurementView(View):
    def post(self, request, pk):
        measurement = get_object_or_404(Measurement, pk=pk)
        if measurement.user != request.user:
            return JsonResponse({'success': False, 'error': 'Not authorized'}, status=403)

        measurement.delete()
        measurements = request.user.measurements.all()
        return JsonResponse({
            'success': True,
            'measurements': [m.to_dict() for m in measurements],
            'message': "Your measurement has been deleted."
        })