# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..user_app.models import *

class Country(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class City(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Neighborhood(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ListingManager(models.Manager):
    def create_listing(self, data, session):
        error = False
        session['address1'] = data['address1']
        session['address2'] = data['address2']
        session['zipcode'] = data['zipcode']
        session['neighborhood'] = data['neighborhood']
        session['city'] = data['city']
        session['country'] = data['country']
        session['description'] = data['description']
        session['price'] = data['price']
        session['sqft'] = data['sqft']
        session['beds'] = data['beds']
        session['baths'] = data['baths']
        session['rent'] = data['rent']
        messages = []
        if len(data['description']) < 2:
            messages.append("description must be at least 2 characters!")
            error = True
        if len(data['address1']) < 2:
            messages.append("address1 must be at least 2 characters!")
            error = True
        else:
            try:
                found_listing = User.objects.get(address1=data['address1'])
            except:
                found_listing = False
            if found_listing:
                messages.append("address1 is already registered!")
                error = True
        if len(data['address2']) < 2:
            messages.append("address2 must be at least 2 characters!")
            error = True
        if len(data['zipcode']) != 5:
            messages.append("zipcode must be 5 digits!")
            error = True
        #elif not ZIPCODE_REGEX.match(data['email']):
        #    messages.append("Please enter a valid email!")
        #    error = True

        if error:
            return {'result':"error", 'messages':messages}
        '''
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(str(data['password']), str(salt))
        User.objects.create(first_name=data['first_name'], last_name=data['last_name'], birthday=data['birthday'],email=data['email'], phone=data['phone'], password=hashed_password, salt=salt)
        user = User.objects.get(email=data['email'])
        session.pop('first_name')
        session.pop('last_name')
        session.pop('email')
        session.pop('phone')
        session.pop('password')
        session.pop('confirm_password')
        session.pop('birthday')
        return {'result':"Successfully registered new user", 'messages':messages, 'user':user}
        '''
class Listing(models.Model):
    address1 = models.CharField(max_length=25)
    address2 = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=5)
    neighborhood = models.ForeignKey(Neighborhood, related_name="neighborhoods")
    city = models.ForeignKey(City, related_name="citys")
    country = models.ForeignKey(Country, related_name="countrys")
    description = models.TextField(max_length=140)
    price = models.IntegerField()
    sqft = models.IntegerField()
    beds = models.SmallIntegerField()
    baths = models.DecimalField(decimal_places=1, max_digits=5) # half ?
    buy = models.BooleanField()
    rent = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="listings")
    favorites = models.ManyToManyField(User, related_name="favorites")
    objects = ListingManager()