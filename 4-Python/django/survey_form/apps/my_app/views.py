# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')

def result(request):
    return render(request, 'survey/result.html')

def submit_survey(request):
    if request.method == "POST":
        if 'count' not in request.session.keys():
            request.session['count'] = 0
        request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    return redirect('/result')