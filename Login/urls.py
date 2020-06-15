from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Login.views import CustonAuthToken

urlpatterns = [
    re_path(r'login', CustonAuthToken.as_view()),
]