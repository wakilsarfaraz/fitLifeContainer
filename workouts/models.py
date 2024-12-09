from django.db import models

class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    youtube_url = models.URLField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_video_id(self):
        # Extracts the video ID from a YouTube URL
        if 'v=' in self.youtube_url:
            return self.youtube_url.split('v=')[-1].split('&')[0]
        elif 'youtu.be/' in self.youtube_url:
            return self.youtube_url.split('youtu.be/')[-1].split('?')[0]
        return None
    

