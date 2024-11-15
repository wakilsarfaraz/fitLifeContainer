from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# ListView to display all posts
class PostView(ListView):
   model = Post
   template_name = 'community.html'
   context_object_name = 'posts'  # This changes the default 'object_list' to 'posts'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['user'] = self.request.user  # Add the current user to the context
       return context

# CreateView to handle the creation of a new post
class AddPostView(CreateView):
   model = Post
   template_name = 'add_post.html'
   form_class = PostForm
   success_url = reverse_lazy('community:community')

   def form_valid(self, form):
      self.object = form.save(commit=False)
      if self.request.user.is_authenticated:
          self.object.user = self.request.user
      else:
        self.object.user = None
      self.object.save()
      return super().form_valid(form)
