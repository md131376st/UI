from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views
from django.conf.urls import url
urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^$', views.signup, name='signup')
    # path('', views.signup, name='signup'),
]
