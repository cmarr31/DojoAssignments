# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt, re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')
ALIAS_REGEX = re.compile(r'^\w+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

class UserManager(models.Manager):
    def login(self, postData):

        failed_authentication = False
        messages = []

        try:
            found_user = User.objects.get(email=postData['email'])
        except:
            found_user = False

        if len(postData['email']) < 1:
            messages.append("Email cannot be left blank!")
            failed_authentication = True
        elif not EMAIL_REGEX.match(postData['email']):
            messages.append("Please enter a valid email!")
            failed_authentication = True
        elif not found_user:
            messages.append("No user found with this email address. Please register new user.")
            failed_authentication = True

        if failed_authentication:
            return {'result':"failed_authentication", 'messages':messages}
        if not PASSWORD_REGEX.match(postData['password']):
            messages.append("Password must be at least 8 characters with at least 1 uppercase letter and 1 numeric value")
            return {'result':"failed_authentication", 'messages':messages}

        hashed_password = bcrypt.hashpw(str(postData['password']), str(found_user.salt))

        if found_user.password != hashed_password:
            messages.append("Incorrect password! Please try again")
            failed_authentication = True


        if failed_authentication:
            return {'result':"failed_authentication", 'messages':messages}
        else:
            messages.append('Successfully logged in!')
            return {'result':'success', 'messages':messages, 'user':found_user}

    def register(self, postData):
        failed_validation = False
        messages = []
        if len(postData['full_name']) < 2:
            messages.append("Name must be at least 2 characters!")
            failed_validation = True
        elif not NAME_REGEX.match(postData['full_name']):
            messages.append("Name can only contain letters or spaces!")
            failed_validation = True
        if len(postData['alias']) < 2:
            messages.append("Alias must be at least 2 characters!")
            failed_validation = True
        elif not ALIAS_REGEX.match(postData['alias']):
            messages.append("Invalid Alias!")
            failed_validation = True
        try:
            found_user = User.objects.get(email=postData['email'])
        except:
            found_user = False
        if len(postData['email']) < 1:
            messages.append("Email is required!")
            failed_validation = True
        elif not EMAIL_REGEX.match(postData['email']):
            messages.append("Please enter a valid email!")
            failed_validation = True
        elif found_user:
            messages.append("This email is already registered!")
            failed_validation = True
        if len(postData['password']) < 1:
            messages.append("Password is required!")
            failed_validation = True
        elif not PASSWORD_REGEX.match(postData['password']):
            messages.append("Password must be at least 8 characters with at least 1 uppercase letter and 1 numeric value")
            failed_validation = True
        elif postData['confirm_password'] != postData['password']:
            messages.append("Password confirmation failed")
            failed_validation = True

        birthday = datetime.strptime(postData['birthday'], '%m/%d/%Y')
        now = datetime.now()
        if len(postData['birthday']) < 1:
            messages.append("Birthday is required!")
            failed_validation = True
        elif birthday >= now:
            messages.append("Birthday is should be a date in the past!")
            failed_validation = True

        if failed_validation:
            return {'result':"failed_validation", 'messages':messages}
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(str(postData['password']), str(salt))
        User.objects.create(full_name=postData['full_name'], alias=postData['alias'], birthday=postData['birthday'],email=postData['email'], password=hashed_password, salt=salt)
        user = User.objects.get(email=postData['email'])
        return {'result':"Successfully registered new user", 'messages':messages, 'user':user}

class User(models.Model):
    full_name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday= models.DateTimeField(auto_now_add=True)
    objects = UserManager()