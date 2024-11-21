from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.classes, name='classes'),
    path('<int:class_id>/', views.class_detail, name='class_detail'),
    path('add_to_calendar/<int:class_id>/', views.add_to_calendar, name='add_to_calendar'),
    path('my_classes/', views.my_classes, name='my_classes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
