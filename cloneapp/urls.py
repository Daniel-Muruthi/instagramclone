from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.landing, name='landingpage'),
    path("emailsignup/", views.signup, name='emailsignup'),
    path("emaillogin/", views.login, name='emaillogin'),
    path("index/", views.userhome, name='index'),
    path("new/", views.new_post, name='newpost'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)