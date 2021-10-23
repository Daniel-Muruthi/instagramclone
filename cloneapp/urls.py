from django.urls import path
from django.conf.urls import include, url
from django.views.generic.edit import DeleteView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import SignUpForm, FindPostView, CreatePostView, DeleteImage, UpdatePostView

app_name = 'cloneapp'
urlpatterns=[
    url(r'^$', views.landing, name='landingpage'),
    path("index/", views.userhome, name='index'),
    path("new/", views.new_post, name='newpost'),
    path("post/new/", CreatePostView.as_view(), name='newerpost'),
    url( r'^emaillogin/$',views.userlogin, name="emaillogin"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url( r'^emailsignup/$',views.signup, name="emailsignup"),
    path('post/<int:pk>/', FindPostView.as_view(), name='findpost'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='updatepost'),
    path('post/<int:pk>/deletepost/', DeleteImage.as_view(), name='delete')
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)