# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("response")
    return render(request, 'index.html')

def results(request, results):
    # VALUES = ['populate this list with various strings']
    print results;
    context = {'results':results}
    return render(request, 'results.html', context)