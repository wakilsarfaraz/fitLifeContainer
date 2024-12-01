from django.urls import path
from .views import measurement_list, add_measurement, edit_measurement, DeleteMeasurementView

urlpatterns = [
    path('', measurement_list, name='measurement_list'), 
    path('add/', add_measurement, name='add_measurement'),
    path('<int:pk>/edit/', edit_measurement, name='edit_measurement'),
    path('<int:pk>/delete/', DeleteMeasurementView.as_view(), name='delete_measurement'),
]