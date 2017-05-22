# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
import random
'''
Landscapes:
Create an app that displays a different image to the user depending upon the value the user enters as a url parameter
Display a different landscape photo depending on the value the user passed in as a route parameter.
Have two templates
Display a different landscape photo for each range of values:
• 1-10: A landscape with snow
• 11-20: A landscape in the desert
• 21-30: A landscape in a forest
• 31-40: A landscape in a vineyard
• 41-50: A tropical landscape
'''
def index(request):
    return render(request, 'index.html')
def results(request, param):
    print type(param)
    context = {'param': int(param)}
    return render(request, 'results.html', context)