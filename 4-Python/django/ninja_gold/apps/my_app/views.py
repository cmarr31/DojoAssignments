# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session.keys():
        request.session['gold'] = 0
    if 'activity_list' not in request.session.keys():
        request.session['activity_list'] = []
    return render(request, 'ninja_gold/index.html')

def process(request, building):
    print request.method
    print building
    if request.method == "POST":
        print "You clicked", building
        earned_gold = 0
        if building == "farm":
            earned_gold = random.randint(10,20)
        elif building == "cave":
            earned_gold = random.randint(5,10)
        elif building == "house":
            earned_gold = random.randint(2,5)
        elif building == "casino":
            if request.session['gold'] <= 50:
                request.session['gold'] = request.session['gold'] # idk why but this is needed otherwise it fails
                request.session['activity_list'].append("You need at least 50 golds to go to the casino! ({})".format(datetime.now()))
                return redirect('/')
            earned_gold = random.randint(-50,50)
            if earned_gold < 0:
                if request.session['gold'] - abs(earned_gold) > 0:
                    print "{} - {} > 0".format(request.session['gold'], earned_gold)
                    request.session['activity_list'].append("Entered a casino and lost {} gold... Ouch. ({})".format(abs(earned_gold), datetime.now()))
                else:
                    request.session['activity_list'].append("Entered a casino and lost all of your gold... Ouch. ({})".format(datetime.now()))
                    request.session['gold'] = 0
                    return redirect('/')
            else:
                request.session['activity_list'].append("Entered a casino and earned {} gold. You got lucky! ({})".format(earned_gold, datetime.now()))
            request.session['gold'] += earned_gold
            return redirect('/')
    request.session['gold'] += earned_gold
    request.session['activity_list'].append("Earned {} gold from the {}! ({})".format(earned_gold, building, datetime.now()))
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')