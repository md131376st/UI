# """untitled URL Configuration
# 
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URL conf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
#
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from first.forms import LoginForm

from first import views as viewsMe

urlpatterns = [
    # url(r'^$', views.Home, name='home'),
    url(r'',include('first.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', viewsMe.signup, {'template_name': 'registration/signup.html', 'next_page': 'registration/home.html'}, name='signup'),
    url(r'^admin/', admin.site.urls),
    url(r'home/$', viewsMe.home, {'template_name': 'registration/home.html'}, name='home'),
    url(r'edit/$', viewsMe.edit, {'template_name': 'registration/profile_edit.html'}, name='edit'),
    url(r'request/$', viewsMe.request, {'template_name': 'registration/request.html', 'next_page':'registration/requestdone.html'}, name='request'),
    url(r'requestdone/$', viewsMe.requestdone, {'template_name': 'registration/requestdone.html'}, name='requestdone')
]
