from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from uuid import uuid4
from product.models import Product


def dashboard(request):
    user = request.user
    if user.is_authenticated:
        return render(request , 'dashboard/dashboard.html' , {'name': user.first_name})
    return redirect('home')

def watch_category(request,category):
    user = request.user
    if user.is_authenticated:
        products = Product.objects.filter(category = category)
        print(products)
        context = {
            'name' : user.first_name ,
            'products' : products
        }
        return render(request , 'dashboard/watch_category.html' , context)
    return redirect('home')