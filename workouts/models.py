from django.db import models

class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    youtube_url = models.URLField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title