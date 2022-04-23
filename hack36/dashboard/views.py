from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from uuid import uuid4
from product.models import Product
from inventory.models import Inventory
import math


def dashboard(request):
    user = request.user
    if user.is_authenticated:
        return render(request , 'dashboard/dashboard.html' , {'name': user.first_name})
    return redirect('home')

def watch_category(request,category):
    user = request.user
    if user.is_authenticated:

        user_lat,user_long = getCoords()

        ax,ay=0,0
        pid=0
        mn=10000000000000

        invents = Inventory.objects.all()

        for x in invents:
            if distance(user_lat,x.locationx,user_long,x.locationy) < mn:
                ax = x.locationx
                ay = x.locationy
                pid = x.id

        # ax,ay are nearest inventory coords and now find products related to pid
        # category = category , id=pid
        # trained ML model will set prices for products

        products = Product.objects.filter(category = category)
        print(products)
        context = {
            'name' : user.first_name ,
            'products' : products
        }
        return render(request , 'dashboard/watch_category.html' , context)
    return redirect('home')

def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
 
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)

def getCoords():
    return {25.90,81.55}