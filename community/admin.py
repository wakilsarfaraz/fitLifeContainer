from django.contrib import admin
from .models import Post, Like, Comment, CommentLike

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'title', 'content', 'image', 'category', 'likes_count')
    
    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()

admin.site.register(Post, PostAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date_liked')
    list_filter = ('post', 'user')

admin.site.register(Like, LikeAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'likes_count', 'parent')
    list_filter = ('post', 'user')

admin.site.register(Comment, CommentAdmin)

class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment')
    list_filter = ('comment', 'user')

admin.site.register(CommentLike, CommentLikeAdmin)