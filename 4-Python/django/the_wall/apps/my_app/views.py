# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from .models import User, Message, Comment

def index(request):
    # create user
    User.objects.create(first_name="MAU", last_name="RUA", email="mau@rua.com", password="123456789")
    users = User.objects.raw("SELECT * from my_app_user")
    for user in users:
        print "user =", user.id, user.first_name, user.last_name, user.email, "*******"
        # create message
        Message.objects.create(user_id=user, message="this is my first message")       
        messages = Message.objects.raw("SELECT * from my_app_message")
        for msg in messages:
            print "message =", msg.id, msg.message
            # create Comment
            Comment.objects.create(message_id=msg, user_id=user, comment="this is my first comment")
            comments = Comment.objects.raw("SELECT * from my_app_comment")
            for com in comments:
                print "comment =", com.id, com.comment

    #mau = User.objects.filter(first_name="MAU")
    #mau.first_name = "XXX"
    #mau.save()
    #mau = User.objects.get(id=7)
    #print "save=", mau.first_name
    #mau = User.objects.get(id=7)
    #print "get =", mau.first_name
    # User.objects.all().delete()
    # print "User.objects.delete() =", User.objects.all()
    return HttpResponse("OK")