from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
      title = models.CharField(max_length=45)
      author = models.CharField(max_length=45)
      published_date = models.CharField(max_length=100)
      category = models.CharField(max_length=45)
      in_print = models.BooleanField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)