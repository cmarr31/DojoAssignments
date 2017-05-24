# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class BookManager(models.Manager):
    def validate(self, postData):
        Book.objects.create(title=postData["title"], author=postData["author"], category=postData["category"], published_date=postData["published_date"])
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    published_date = models.CharField(max_length=100)
    category = models.CharField(max_length=45)
    in_print = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
    def __str__(self):
        return self.title + " " + self.author + " " + self.category