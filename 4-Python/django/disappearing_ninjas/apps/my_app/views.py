# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("No ninjas here")

def ninjas(request):
    return render(request, 'index.html')

def ninja(request, color):
    print color;
    context = {'color':color}
    return render(request, 'ninja.html', context)