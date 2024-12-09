from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, DetailView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count

from .forms import PostForm

from django.db.models import Count
from .models import Post, Like, Comment , CommentLike 


class PostView(ListView):
    model = Post
    template_name = 'community.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all().annotate(comments_count=Count('comments'))

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)

        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'newest':
            queryset = queryset.order_by('-date')
        elif sort_by == 'oldest':
            queryset = queryset.order_by('date')
        elif sort_by == 'alpha':
            queryset = queryset.order_by('title')
        elif sort_by == 'likes':
            queryset = queryset.order_by('-likes_count')

        my_posts = self.request.GET.get('my_posts')
        if my_posts == 'true' and self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['categories'] = Post.objects.values_list('category', flat=True).distinct()
        context['current_category'] = self.request.GET.get('category', '')
        context['current_sort'] = self.request.GET.get('sort_by', '')
        context['my_posts'] = self.request.GET.get('my_posts') == 'true'
        return context 

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs['pk'])
        comments = post.comments.filter(parent=None)

        for comment in comments:
            comment.likes_count = comment.likes.count()  # Count likes using the related_name 'likes'
        
        return render(request, 'post_detail.html', {
            'post': post,
            'comments': comments,

        })
 

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
        messages.success(self.request, "Your post has been added.")
        return super().form_valid(form)


class DeletePostView(View):
    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        if post.user != request.user:
            messages.error(request, "You are not authorized to delete this post.")
            return redirect('community:community')

        post.delete()
        messages.success(request, "Your post has been deleted.")
        return redirect('community:community')


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()
        post.likes_count -= 1
    else:
        post.likes_count += 1

    post.save()
    messages.success(request, "You liked this post!" if created else "You unliked this post.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content').strip()
        parent_id = request.POST.get('parent_id')
        if not content:
            messages.error(request, "Comment content cannot be empty.")
            return redirect('community:post_detail', pk=post_id)

        if parent_id:
            parent = get_object_or_404(Comment, id=parent_id)
            Comment.objects.create(user=request.user, post=post, parent=parent, content=content)
        else:
            Comment.objects.create(user=request.user, post=post, content=content)
    return redirect('community:post_detail', pk=post_id)




@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect('community:post_detail', pk=comment.post.id)

    comment.delete()
    messages.success(request, "Your comment has been deleted.")
    return redirect('community:post_detail', pk=comment.post.id)

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like, created = CommentLike.objects.get_or_create(user=request.user, comment=comment)

    if not created:
        like.delete()
        comment.likes_count -= 1
    else:
        comment.likes_count += 1

    comment.save()
    messages.success(request, "You liked this comment!" if created else "You unliked this comment.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))