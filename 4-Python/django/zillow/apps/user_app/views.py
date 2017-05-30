# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import get_messages
from django.contrib import messages
from django.db.models import Count
from django.core.urlresolvers import reverse
from .models import *

def index(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, "user_app/index.html", context)