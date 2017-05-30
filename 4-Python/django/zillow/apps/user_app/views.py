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
    if "current_user" in request.session.keys():
        user = User.objects.get(pk=request.session['current_user'])
        context['user'] = user
    return render(request, "user_app/index.html", context)

def join(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, "user_app/register.html", context)

def sign_in(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, "user_app/login.html", context)

def register(request):
    if request.method == "POST":
        data = {
            'first_name':request.POST['first_name'],
            'last_name':request.POST['last_name'],
            'email':request.POST['email'],
            'birthday':request.POST['birthday'],
            'password':request.POST['password'],
            'confirm_password':request.POST['confirm_password']
        }
        register_result = User.objects.register(data, request.session)
        if register_result['result'] == "failed_validation":
            if 'messages' in register_result.keys():
                for message in register_result['messages']:
                    messages.error(request, message)
            return redirect(reverse('user_app:join'))
        else:
            if 'user' in register_result.keys():
                request.session['current_user'] = register_result['user'].id
                if 'messages' in register_result.keys():
                    for message in register_result['messages']:
                        messages.success(request, message)
            return redirect(reverse('user_app:index'))
    return redirect(reverse('user_app:index'))

def login(request):
    if request.method == "POST":
        data = {
            'email':request.POST['email'],
            'password':request.POST['password']
        }
        login_result = User.objects.login(data)
        if login_result['result'] == "failed_authentication":
            if 'messages' in login_result.keys():
                for message in login_result['messages']:
                    messages.error(request, message)
            return redirect(reverse('user_app:sign_in'))
        else:
            if 'user' in login_result.keys():
                request.session['current_user'] = login_result['user'].id
            return redirect(reverse('user_app:index'))

def logout(request):
    request.session.clear()
    return redirect(reverse('user_app:index'))

def show_user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        "user":user,
    }
    return render(request, "user_app/user_profile.html", context)