from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from django.contrib.auth.models import User

from Example2 import views

urlpatterns = [
    re_path(r'/example2/$', views.ExampleList.as_view()),
]