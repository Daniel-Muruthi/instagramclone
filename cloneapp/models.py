from django.db import models
import datetime as dt
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.contrib import auth


class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

class HashTag(models.Model):
    hashtag=models.CharField(max_length=30)

    def __str__(self):
        return self.hashtag

class Comment(models.Model):
    userpost = models.IntegerField
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def savecomment(self):
        self.save()

class Post(models.Model):
    image = CloudinaryField('image')
    author = models.CharField(max_length = 60)
    postcaption = HTMLField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hashtag = models.ManyToManyField(HashTag)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True, max_length=500)


    @classmethod
    def show_posts(cls):
        posts = cls.objects.all()
        return posts


class UserProfile(models.Model):
    title= models.CharField(max_length=255),
    username = models.ForeignKey(User, on_delete=models.CASCADE),
    email = models.CharField(max_length=255),
    phonenumber = models.IntegerField(),
    bio = models.CharField(max_length=255),
    userpic = CloudinaryField('image')

    def __str__(self):
        return self.username


# class User(auth.models.User, auth.models.PermissionMixin):
#     readonly_fields = ('id', 'pk')

#     def __str__(self):
#         return self.username