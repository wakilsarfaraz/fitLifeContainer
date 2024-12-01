from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('community/', include(('community.urls', 'community'), namespace='community')),
    path('classes/', include(('classes.urls', 'classes'), namespace='classes')),
    path('workouts/', include(('workouts.urls', 'workouts'), namespace='workouts')),
    path('userauth/', include(('userauth.urls', 'userauth'), namespace='userauth')),
    path('measurements/', include(('measurements.urls', 'measurements'), namespace='measurements')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
