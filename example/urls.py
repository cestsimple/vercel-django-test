# coding=utf-8
# example/urls.py
from django.urls import path

from .views import index

urlpatterns = [
    path('', index),
]
