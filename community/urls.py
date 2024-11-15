from django.urls import path
from .views import AddPostView
from .views import PostView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'community'
urlpatterns = [
    path('',PostView.as_view(),name='community'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
]+ static (settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
