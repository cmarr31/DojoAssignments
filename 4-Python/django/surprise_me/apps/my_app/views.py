# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
import random
VALUES = ['strange', 'weird', 'unusual', 'rare', 'different', 'wicked', 'odd', 'crazy', 'eccentric', 'queer', 'singular', 'funky', 'freaky', 'curious', 'uncanny']
'''
Surprise Me! 
Make an app that serves up whichever number of random items the user requests.
If the user enters '3' display 3 items on the next page.
At the top of your views.py, under your module imports add: VALUES = ['populate this list with various strings']
When a user enters a number and submits the form, shuffle the list of strings. 
You can access the above list from any view function. 
Return to the template n number of elements from the front of the list, where n is the value the user entered.
Display the strings in the template.
'''
def index(request):
    return render(request, 'index.html')
def results(request):
    random.shuffle(VALUES)
    if request.session['number']=="0":
        return render(request, 'results.html')
    else:
        context = {'values':VALUES[0:int(request.session['number'])]}
        return render(request, 'results.html', context)
    
def submit(request):
    if request.method == "POST":
        request.session['number'] = request.POST['number']
    return redirect('/results')