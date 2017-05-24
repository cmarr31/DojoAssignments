# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
import re
from .models import Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# TODO: move logic from view to model

def index(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, 'index.html', context)

def validation_check(request):
    if request.method == "POST":
        email = request.POST['email']
        if len(email) < 1:
            messages.error(request, "Email cannot be left blank!")
        elif EMAIL_REGEX.match(email):
            print "Inserting into database"
            Email.objects.create(email=email)
            print Email.objects.all()
            messages.success(request, "The email address you entered (" + email + ") is a VALID email address! Thank you!")
            return redirect('/emails')
        else:
            messages.error(request, "Please Enter a Valid Email Address!")
    return redirect('/')

def display_email_list(request):
    context = {
        'messages':get_messages(request),
        'all_emails':Email.objects.all()
    }
    return render(request, 'emails.html', context)

def delete_email(request, email_id):
    Email.objects.get(pk=email_id).delete()
    return redirect('/emails')