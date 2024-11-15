# models.py

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Model to represent a post
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=1000, default='Default Subject')
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    likes_count = models.PositiveIntegerField(default=0)  # Field to track the number of likes

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


# Model to represent a 'like' action on a post
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # Prevent a user from liking the same post multiple times

    def __str__(self):
        return f"{self.user.username} liked {self.post.subject}"
