# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(related_name='books', to='my_app.User'),
        ),
    ]
