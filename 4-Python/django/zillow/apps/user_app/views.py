# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import get_messages
from django.contrib import messages
from django.db.models import Count
from django.core.urlresolvers import reverse

from .models import *

def join(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, "user_app/new_user.html", context)

def sign_in(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, "user_app/login.html", context)

def create_user(request):
    if request.method == "POST":
        data = {
            'first_name':request.POST['first_name'],
            'last_name':request.POST['last_name'],
            'email':request.POST['email'],
            'phone':request.POST['phone'],
            'birthday':request.POST['birthday'],
            'password':request.POST['password'],
            'confirm_password':request.POST['confirm_password']
        }
        result = User.objects.create_user(data, request.session)
        if result['result'] == "error":
            if 'messages' in result.keys():
                for message in result['messages']:
                    messages.error(request, message)
            return redirect(reverse('user_app:join'))
        if 'user' in result.keys():
            request.session['current_user'] = result['user'].id
            if 'messages' in result.keys():
                for message in result['messages']:
                    messages.success(request, message)
    return redirect(reverse('listing_app:index'))

def login(request):
    if request.method == "POST":
        data = {
            'email':request.POST['email'],
            'password':request.POST['password']
        }
        login_result = User.objects.login(data)
        if login_result['result'] == "error":
            if 'messages' in login_result.keys():
                for message in login_result['messages']:
                    messages.error(request, message)
            return redirect(reverse('user_app:sign_in'))
        if 'user' in login_result.keys():
            request.session['current_user'] = login_result['user'].id
        return redirect(reverse('listing_app:index'))

def logout(request):
    request.session.clear()
    return redirect(reverse('listing_app:index'))

def show_user(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        "user":user,
    }
    return render(request, "user_app/user.html", context)