# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random, string

# Create your views here.


def index(request):

    return render(request, "generator/index.html")


def generate(request):

    if request.method == "POST":

        if 'counter' not in request.session.keys():
            request.session['counter'] = 0
        request.session['counter'] += 1
        request.session['generated_word'] = ''.join(random.choice(string.uppercase) for i in range(14))

    return redirect('/')
