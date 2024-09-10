from django.db import models

# Create your models here.


class BlogModels(models.Model):
    title = models.CharField(max_length=500)
    detail = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    youtube_Title = models.CharField(max_length=500)
    youtube_link = models.URLField(blank=True)


    def __str__(self):
        return self.title