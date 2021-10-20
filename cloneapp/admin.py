from django.contrib import admin
from .models import HashTag, Location, Post
from django.contrib.admin import AdminSite
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('hashtag',)

admin.site.register(Location)
admin.site.register(Post, PostAdmin)
admin.site.register(HashTag)