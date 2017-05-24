# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import Course

def index(request):
    courses = Course.objects.all()
    context = {
        "courses":courses
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        data={
            "course_name":request.POST["course_name"],
            "course_description":request.POST["course_description"]
        }
        Course.objects.validate(data)
    return redirect('/')

def confirm(request, course_id):
    course = Course.objects.get(pk=course_id)
    context = {
        "course":course
    }
    return render(request, "confirm.html", context)

def delete(request, course_id):
    data={
        "course_id": course_id
    }
    Course.objects.delete(data)
    return redirect('/')