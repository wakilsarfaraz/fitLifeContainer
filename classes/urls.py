 
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.classes, name='classes'),
    path('my-classes/', views.my_classes, name='my_classes'),
    path('<int:class_id>/add/', views.add_to_my_classes, name='add_to_my_classes'),
    path('<int:class_id>/remove/', views.remove_from_my_classes, name='remove_from_my_classes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
