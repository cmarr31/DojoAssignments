# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt, re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')
# ALIAS_REGEX = re.compile(r'^\w+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

class UserManager(models.Manager):
    def login(self, data):

        failed_authentication = False
        messages = []

        try:
            found_user = User.objects.get(email=data['email'])
        except:
            found_user = False

        if len(data['email']) < 1:
            messages.append("Email cannot be left blank!")
            failed_authentication = True
        elif not EMAIL_REGEX.match(data['email']):
            messages.append("Please enter a valid email!")
            failed_authentication = True
        elif not found_user:
            messages.append("No user found with this email address. Please register new user.")
            failed_authentication = True

        if failed_authentication:
            return {'result':"failed_authentication", 'messages':messages}
        if not PASSWORD_REGEX.match(data['password']):
            messages.append("Password must be at least 8 characters with at least 1 uppercase letter and 1 numeric value")
            return {'result':"failed_authentication", 'messages':messages}

        hashed_password = bcrypt.hashpw(str(data['password']), str(found_user.salt))

        if found_user.password != hashed_password:
            messages.append("Incorrect password! Please try again")
            failed_authentication = True


        if failed_authentication:
            return {'result':"failed_authentication", 'messages':messages}
        else:
            messages.append('Successfully logged in!')
            return {'result':'success', 'messages':messages, 'user':found_user}

    def register(self, data, session):
        failed_validation = False
        session['first_name'] = data['first_name']
        messages = []
        if len(data['first_name']) < 2:
            messages.append("Name must be at least 2 characters!")
            failed_validation = True
        elif not NAME_REGEX.match(data['first_name']):
            messages.append("First Name can only contain letters or spaces!")
            failed_validation = True
        if len(data['last_name']) < 2:
            messages.append("last_name must be at least 2 characters!")
            failed_validation = True
        elif not NAME_REGEX.match(data['last_name']):
            messages.append("Last Name can only contain letters or spaces!")
            failed_validation = True
        try:
            found_user = User.objects.get(email=data['email'])
        except:
            found_user = False
        if len(data['email']) < 1:
            messages.append("Email is required!")
            failed_validation = True
        elif not EMAIL_REGEX.match(data['email']):
            messages.append("Please enter a valid email!")
            failed_validation = True
        elif found_user:
            messages.append("This email is already registered!")
            failed_validation = True
        if len(data['password']) < 1:
            messages.append("Password is required!")
            failed_validation = True
        elif not PASSWORD_REGEX.match(data['password']):
            messages.append("Password must be at least 8 characters with at least 1 uppercase letter and 1 numeric value")
            failed_validation = True
        elif data['confirm_password'] != data['password']:
            messages.append("Password confirmation failed")
            failed_validation = True

        now = datetime.now()
        if len(data['birthday']) < 1:
            messages.append("Birthday is required!")
            failed_validation = True
        
        else:
            birthday = datetime.strptime(data['birthday'], '%Y-%m-%d')
            # birthday = datetime.strptime(data['birthday'], '%m/%d/%Y')
            # birthday = datetime.strptime(data['birthday'], '%Y-%-%d')
            if birthday >= now:
                messages.append("Birthday is should be a date in the past!")
                failed_validation = True

        if failed_validation:
            return {'result':"failed_validation", 'messages':messages}
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(str(data['password']), str(salt))
        User.objects.create(first_name=data['first_name'], last_name=data['last_name'], birthday=data['birthday'],email=data['email'], password=hashed_password, salt=salt)
        user = User.objects.get(email=data['email'])
        session.pop('first_name')
        return {'result':"Successfully registered new user", 'messages':messages, 'user':user}

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday= models.DateTimeField(auto_now_add=True)
    objects = UserManager()