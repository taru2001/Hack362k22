from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from uuid import uuid4

def home(request):
    user = request.user
    log=0
    if user.is_authenticated:
        log=1
        return redirect('dashboard')
    return render(request , "home/home.html" , {'log':log})

def signup(request):
    if request.method == 'POST':
        print("reached")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        mobile = request.POST.get('mobile',"")
        password = request.POST.get('password',"")
        cpassword = request.POST.get('cpassword',"")

        if(password != cpassword):
            return redirect('home')

        all_users = User.objects.all()

        for user in all_users:
            if user.email == email:
                return redirect('home')

        curr_user=User.objects.create_user(email,email,password)
        curr_user.first_name=name
        curr_user.last_name=name
        curr_user.save()
        print("registered")

        user = authenticate(username = email , password = password)

        if user :
            login(request,user)
            return redirect('dashboard')

        

        return redirect('home')

def login_user(request):
    user = request.user

    if user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        femail = request.POST.get('email',"")
        fpassword = request.POST.get('password',"")
        
        all_users = User.objects.all()

        conf_user = authenticate(username=femail,password=fpassword)

        if conf_user:
            login(request,conf_user)
            return redirect('dashboard')

    return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('home')

        
