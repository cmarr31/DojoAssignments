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
    return render(request, "time_display_app/index.html")