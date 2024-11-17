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
            queryset = queryset.order_by('date')  # Oldest first
        elif sort_by == 'alpha':
            queryset = queryset.order_by('subject')  # Alphabetical order by subject
        elif sort_by == 'likes':
            queryset = queryset.annotate(num_likes=Count('likes')).order_by('-num_likes')  # Most liked first

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Add the current user to the context
        return context

# Like/unlike functionality for a post
def like_post(request, post_id):
    """Handles liking and unliking a post without raising an error if the post is already liked."""
    if not request.user.is_authenticated:
        return redirect('login')  # Ensure the user is logged in

    post = get_object_or_404(Post, id=post_id)
    
    # Check if the user has already liked the post
    like_instance = Like.objects.filter(user=request.user, post=post).first()
    
    if like_instance:
        # If the user has liked the post, remove the like (unlike it)
        like_instance.delete()
    else:
        # If the user hasn't liked the post, add a new like
        Like.objects.create(user=request.user, post=post)

    # Update the likes_count for the post based on the related Like objects
    post.likes_count = post.likes.count()  # This will update the count based on the related Like objects
    post.save()

    # Redirect back to the community page after toggling the like
    return redirect('community:community')  # Redirect to the community page

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
