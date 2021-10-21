from django.db import models
import datetime as dt
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from cloudinary.models import CloudinaryField


class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

class HashTag(models.Model):
    hashtag=models.CharField(max_length=30)

    def __str__(self):
        return self.hashtag

class Post(models.Model):
    image = CloudinaryField('image')
    author = models.CharField(max_length = 60)
    postcaption = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hashtag = models.ManyToManyField(HashTag)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True, max_length=500)


    @classmethod
    def show_posts(cls):
        posts = cls.objects.all()
        return posts
