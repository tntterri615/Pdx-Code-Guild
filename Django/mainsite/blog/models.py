from django.db import models
from django.conf.urls import url
from django.utils import timezone
from django.contrib.auth.models import User, Group, Permission


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


