"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from cloneapp import views
from cloneapp.views import FindPostView 

# class MyRegistrationView(RegistrationView):
#     def get_success_url(self, request, user):
#         return '/cloneapp/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cloneapp.urls')),

    # path('', include('registration.backends.simple.urls')),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^logout/$', auth_views.LogoutView.as_view(), {"next_page": '/'}),
    # url( r'^emaillogin/$',views.userlogin, name="emaillogin"),
    # url( r'^emailsignup/$',views.signup, name="emailsignup"),
    # url(r'^accounts/register/$', MyRegistrationView.as_view, name="register", ),
    # url(r'^accounts/login/$', auth_views.LoginView.as_view(), name="login")


]
