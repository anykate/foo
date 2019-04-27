from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Topic(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    published_on = models.DateTimeField(null=True, blank=True)
    topics = models.ManyToManyField(Topic, related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
