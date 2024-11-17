# community/urls.py

from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.PostView.as_view(), name='community'),  # List all posts
    path('add/', views.AddPostView.as_view(), name='add_post'),  # Add new post
    path('like/<int:post_id>/', views.like_post, name='like_post'),  # Like/unlike post
]
