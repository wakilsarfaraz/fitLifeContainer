
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.PostView.as_view(), name='community'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('add/', views.AddPostView.as_view(), name='add_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
]
