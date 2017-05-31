# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import get_messages
from django.contrib import messages
from django.db.models import Count
from django.core.urlresolvers import reverse

from .models import *

def new_listing(request):
    context = {
        'messages':get_messages(request)
    }
    if "current_user" in request.session.keys():
        user = User.objects.get(pk=request.session['current_user'])
        context['user'] = user
    return render(request, "listing_app/listing.html", context)

def create_listing(request):
    if request.method == "POST":
        data = {
            'description':request.POST['description'],
            'address1':request.POST['address1'],
            'address2':request.POST['address2'],
            'zipcode':request.POST['zipcode'],
            'price':request.POST['price'],
            'sqft':request.POST['sqft'],
            'beds':request.POST['beds'],
            'baths':request.POST['baths'],
            'rent':request.POST['rent'],
            'user':request.POST['user']
        }

        if "neighborhood" in request.POST.keys():
            data['neighborhood']  = request.POST['neighborhood']
        elif "new-neighborhood" in request.POST.keys():
            data['neighborhood'] = request.POST['new-neighborhood']
        else:
            data['neighborhood'] = ""

        if "city" in request.POST.keys():
            data['city'] = request.POST['city']
        elif "new-city" in request.POST.keys():
            data['city'] = request.POST['new-city']
        else:
            data['city'] = ""
        
        if "country" in request.POST.keys():
            data['country'] = request.POST['country']
        elif "new-country" in request.POST.keys():
            data['country'] = request.POST['new-country']
        else:
            data['country'] = ""

        result = Listing.objects.create_listing(data, request.session)
        if result['result'] == "error":
            if 'messages' in result.keys():
                for message in result['messages']:
                    messages.error(request, message)
            return redirect(reverse('listing_app:new_listing'))
        if 'user' in result.keys():
            request.session['current_user'] = result['user'].id
            if 'messages' in result.keys():
                for message in result['messages']:
                    messages.success(request, message)
    return redirect(reverse('user_app:index'))