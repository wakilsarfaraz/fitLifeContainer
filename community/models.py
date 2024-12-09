import os
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default='Default Title') # Updated field
    content = models.TextField() # Renamed description to content
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=100, choices=[
    ('workout', 'Workout'),
    ('diet', 'Diet'),
    ('transformation', 'Transformation'),
    ('general', 'General'),
    ], default='general') # New field for predefined categories
    likes_count = models.PositiveIntegerField(default=0)


    def get_absolute_url(self):
        return reverse('community')

    def like(self):
        """Method to increment likes count"""
        self.likes_count += 1
        self.save()

    def unlike(self):
        """Method to decrement likes count"""
        if self.likes_count > 0:
            self.likes_count -= 1
            self.save()

    def get_likes(self):
        """Returns the current number of likes"""
        return self.likes_count

    @property
    def liked_by(self):
        """Returns the users who liked this post"""
        return self.likes.all()
    
    class Meta:
        db_table = "posts"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "likes"
        unique_together = ('user', 'post')  # Prevent a user from liking the same post multiple times

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    content = models.TextField()
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.content[:50]}'
    
    class Meta:
        db_table = "comments"
    

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    class Meta:
        db_table = "comment_likes"
        unique_together = ('user', 'comment')

    def __str__(self):
        return f'{self.user.username} liked {self.comment}'