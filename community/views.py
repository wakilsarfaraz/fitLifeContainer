from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Post, Like, Comment, CommentLike
from .forms import PostForm, CommentForm

class PostView(ListView):
    model = Post
    template_name = 'community.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all()
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'newest':
            queryset = queryset.order_by('-date')
        elif sort_by == 'oldest':
            queryset = queryset.order_by('date')
        elif sort_by == 'alpha':
            queryset = queryset.order_by('subject')
        elif sort_by == 'likes':
            queryset = queryset.annotate(num_likes=Count('likes')).order_by('-num_likes')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    success_url = reverse_lazy('community:community')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.user.is_authenticated:
            self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    post.likes_count = post.likes.count()
    post.save()
    return JsonResponse({'liked': created, 'likes_count': post.likes_count})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')
        if parent_id:
            parent = get_object_or_404(Comment, id=parent_id)
            Comment.objects.create(user=request.user, post=post, parent=parent, content=content)
        else:
            Comment.objects.create(user=request.user, post=post, content=content)
    return redirect('community:post_detail', pk=post_id)

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like, created = CommentLike.objects.get_or_create(user=request.user, comment=comment)
    if not created:
        like.delete()
    comment.likes_count = comment.likes.count()
    comment.save()
    return redirect('community:post_detail', pk=comment.post.id)