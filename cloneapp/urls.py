from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import SignUpForm


urlpatterns=[
    url(r'^$', views.landing, name='landingpage'),
    # path("registration_form/", views.signup, name='emailsignup'),
    # path("emaillogin/", views.login, name='emaillogin'),
    path("index/", views.userhome, name='index'),
    path("new/", views.new_post, name='newpost'),
    path("new/newpost/", views.newpost, name='newerpost'),
    url( r'^emaillogin/$',views.userlogin, name="emaillogin"),
    url(r'^logout/$', views.logout, name='logout'),
    url( r'^emailsignup/$',views.signup, name="emailsignup"),
    
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)