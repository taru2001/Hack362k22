from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from uuid import uuid4


def dashboard(request):
    user = request.user
    if user.is_authenticated:
        return render(request , 'dashboard/dashboard.html' , {'name': user.first_name})
    return redirect('home')

def fruits(request):
    user = request.user
    if user.is_authenticated:
        return render(request , 'dashboard/fruits.html' , {'name' : user.first_name})
    return redirect('home')