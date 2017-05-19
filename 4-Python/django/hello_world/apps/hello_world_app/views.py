# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#CONTROLLER
from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

# the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    # return HttpResponse(response)
    return render(request, "index.html")