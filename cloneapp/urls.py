from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$', views.landing, name='landingpage'),
    path("emailsignup/", views.signup, name='emailsignup'),
    path("emaillogin/", views.login, name='emaillogin'),
    path("index/", views.userhome, name='index'),
    path("new/", views.new_post, name='newpost'),
    path("new/newpost/", views.newpost, name='newerpost'),
    # url( r'^emaillogin/$',auth_views.LoginView.as_view(template_name="registration/emaillogin.html"), name="emaillogin"),
    # url( r'^emailsignup/$',auth_views.LoginView.as_view(template_name="registration/emailsignup.html"), name="emailsignup"),
    
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)