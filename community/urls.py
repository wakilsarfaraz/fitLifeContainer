from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='community'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/add/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('post/delete/<int:id>/', views.DeletePostView.as_view(), name='delete_post'),
]
