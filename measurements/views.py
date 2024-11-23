from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Measurement
from .forms import MeasurementForm

# Display all measurements for the logged-in user
@login_required
def measurement_list(request):
    measurements = Measurement.objects.filter(user=request.user).order_by('-date')
    return render(request, 'measurement_list.html', {'measurements': measurements})

# Add a new measurement
@login_required
def add_measurement(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user  # Associate measurement with logged-in user
            measurement.save()
            return redirect('measurement_list.html')
    else:
        form = MeasurementForm()
    return render(request, 'measurement_list.html', {'form': form})

# Edit a measurement
@login_required
def edit_measurement(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MeasurementForm(request.POST, instance=measurement)
        if form.is_valid():
            form.save()
            return redirect('measurement_list.html')
    else:
        form = MeasurementForm(instance=measurement)
    return render(request, 'measurement_list.html', {'form': form})

# Delete a measurement
@login_required
def delete_measurement(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk, user=request.user)
    measurement.delete()
    return redirect('measurement_list.html')

# API endpoint to fetch a measurement's data (used for editing in the modal)
@login_required
def measurement_detail(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk, user=request.user)
    data = {
        'weight': measurement.weight,
        'height': measurement.height,
        'chest': measurement.chest,
        'waist': measurement.waist,
        'hips': measurement.hips,
        'thighs': measurement.thighs,
        'calves': measurement.calves,
        'left_arm': measurement.left_arm,
        'right_arm': measurement.right_arm,
        'bmi': measurement.bmi,
    }
    return JsonResponse(data)
