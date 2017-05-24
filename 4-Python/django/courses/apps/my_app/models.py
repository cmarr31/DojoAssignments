# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validate(self, postData):
        Course.objects.create(course_name=postData["course_name"], course_description=postData["course_description"])
    def delete(self, postData):
        Course.objects.get(pk=postData["course_id"]).delete()
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    def __str__(self):
        return self.course_name