from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('category/<str:category>/' , views.watch_category , name='fruits')
]