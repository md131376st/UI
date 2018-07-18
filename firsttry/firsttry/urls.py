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

from first import views


urlpatterns = [
    # url(r'^$', views.Home, name='home'),
    url(r'',include('first.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, {'template_name': 'registration/signup.html', 'next_page': 'registration/home.html'}, name='signup'),
    url(r'^admin/', admin.site.urls),
    url(r'home/$', views.home, {'template_name': 'registration/home.html'}, name='home'),
    url(r'edit/$', views.edit, {'template_name': 'registration/profile_edit.html'}, name='edit'),
    url(r'request/$' ,views.request, {'template_name': 'reqistration/request.html'}, name='request')
]
