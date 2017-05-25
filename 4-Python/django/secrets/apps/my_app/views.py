# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
import re, bcrypt
from .models import User, Secret
from django.db.models import Count

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

def login_page(request):
    if "current" in request.session.keys():
        print request.session['current_user']
    else:
        print "There is no user currently logged in"
    context = {
        'messages':get_messages(request)
    }
    return render(request, 'my_app/index.html', context)

def registration_page(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, 'my_app/register.html', context)

def authenticate_login(request):
    if request.method == "POST":
        post_data = {
            'email':request.POST['email'],
            'password':request.POST['password']
        }
        login_result = User.objects.login(post_data)
        print login_result
        if login_result['result'] == "failed_authentication":
            print "login result returned failed authentication"
            if 'messages' in login_result.keys():
                for message in login_result['messages']:
                    messages.error(request, message)
            return redirect('/')
        else:
            if 'user' in login_result.keys():
                request.session['current_user'] = login_result['user'].id
                if 'messages' in login_result.keys():
                    for message in login_result['messages']:
                        messages.success(request, message)
            else:
                messages.error(request, "Something went wrong")
                return redirect('/')
            return redirect('/secrets')

def process_registration(request):
    if request.method == "POST":
        post_data = {
            'first_name':request.POST['first_name'],
            'last_name':request.POST['last_name'],
            'email':request.POST['email'],
            'password':request.POST['password'],
            'confirm_password':request.POST['confirm_password']
        }
        register_result = User.objects.register(post_data)
        print register_result
        if register_result['result'] == "failed_validation":
            if 'messages' in register_result.keys():
                for message in register_result['messages']:
                    messages.error(request, message)
            return redirect('/register')
        else:
            if 'user' in register_result.keys():
                request.session['current_user'] = register_result['user'].id
                if 'messages' in register_result.keys():
                    for message in register_result['messages']:
                        messages.success(request, message)
            else:
                messages.error(request, "Something went wrong")
                return redirect('/register')
            return redirect('/secrets')
    return redirect('/register')

def show_secret_page(request):
    if "current_user" in request.session.keys():
        context = {
            "user":User.objects.get(pk=request.session['current_user']),
            "messages":get_messages(request),
            "secrets":Secret.objects.all().annotate(num_likes=Count('likes')).order_by('-created_at')[:5]
        }
        return render(request, 'my_app/secrets.html', context)
    return render(request, 'my_app/mysecrets.html')

def show_most_popular(request):
    if "current_user" in request.session.keys():
        context = {
            "user":User.objects.get(pk=request.session['current_user']),
            "messages":get_messages(request),
            "secrets":Secret.objects.all().annotate(num_likes=Count('likes')).order_by('-num_likes')
        }

        return render(request, 'my_app/most_popular.html', context)
    return render(request, 'my_app/most_popular.html')

def create_new_secret(request, user_id):
    if request.method == "POST":
        Secret.objects.create(content=request.POST['content'], author=User.objects.get(pk=user_id))
    return redirect('/secrets')

def delete_secret(request, secret_id, return_loc):
    # if request.method == "POST":
    Secret.objects.get(pk=secret_id).delete()
    return redirect('/' + return_loc)

def like_secret(request, secret_id, user_id, return_loc):
    secret = Secret.objects.get(pk=secret_id)
    user = User.objects.get(pk=user_id)
    if user not in secret.likes.all():
        secret.likes.add(user)
    return redirect('/' + return_loc)

def unlike_secret(request, secret_id, user_id, return_loc):
    secret = Secret.objects.get(pk=secret_id)
    user = User.objects.get(pk=user_id)
    if user in secret.likes.all():
        secret.likes.remove(user)
    return redirect('/' + return_loc)

def log_out_user(request):
    request.session.clear()
    messages.success(request, "Successfully logged out")
    return redirect('/')