# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=38)),
                ('weight', models.CharField(max_length=38)),
                ('price', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('category', models.CharField(max_length=38)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
