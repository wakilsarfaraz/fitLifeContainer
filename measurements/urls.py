from django.urls import path
from . import views

app_name = 'measurements'

urlpatterns = [
    path('', views.measurement_list, name='measurement_list'),
    path('add/', views.add_measurement, name='add_measurement'),
    path('<int:pk>/edit/', views.edit_measurement, name='edit_measurement'),
    path('<int:pk>/delete/', views.delete_measurement, name='delete_measurement'),
]
