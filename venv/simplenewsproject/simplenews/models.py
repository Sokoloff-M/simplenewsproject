from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    hidden = models.BooleanField(default=False)

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    hidden = models.BooleanField(default=False)
    #