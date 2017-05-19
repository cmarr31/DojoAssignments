# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.shortcuts import render
# Create your views here.

#CONTROLLER
from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

# the index function is called when root is visited
def index(request):
    #response = "Hello, I am your first request!"
    #return HttpResponse(response)
    request.session['upper_date'] = "{:%b %d, %Y}".format(datetime.now())
    request.session['lower_date'] = "{:%I:%M %p}".format(datetime.now()) 
    return render(request, "first_app/index.html")

def testimonials(request):
	print request.method
	return render(request, "first_app/testimonials.html")

def about(request):
	print request.method
	return render(request, "first_app/about.html")

def projects(request):
	print request.method
	return render(request, "first_app/projects.html")
    
def create(request):
    print request.method
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)
        request.session["name"] = request.POST["first_name"]
        return redirect("/")
    else:
	    return redirect("/")