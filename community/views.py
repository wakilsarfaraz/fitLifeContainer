from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post, Like
from .forms import PostForm
from django.db.models import Count  # Needed for the annotation

# ListView to display all posts
class PostView(ListView):
    model = Post
    template_name = 'community.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all()

        sort_by = self.request.GET.get('sort_by')

        if sort_by == 'newest':
            queryset = queryset.order_by('-date')  # Most recent first
        elif sort_by == 'oldest':
            qu