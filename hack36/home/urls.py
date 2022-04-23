from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('',views.home , name='home'),
    path('signup/' , views.signup , name='signup'),
    path('login/' , views.login_user , name='login'),
    path('logout/' , views.logout_user , name = 'logout')
]