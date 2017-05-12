import random
from flask import Flask, render_template, redirect, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dojo"

@app.route('/')
def main_page():

    if 'gold' not in session.keys():
        session['gold'] = 0
    if 'activity_list' not in session.keys():
        session['activity_list'] = []

    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process_money():
    choice = request.form['building']
    print "You clicked", choice

    earned_gold = 0

    if choice == "farm":
        earned_gold = random.randint(10,20)
    elif choice == "cave":
        earned_gold = random.randint(5,10)
    elif choice == "house":
        earned_gold = random.randint(2,5)
    elif choice == "casino":
        if session['gold'] <= 0:
            session['activity_list'].append("You can't go to the casino if you don't have any gold! ({})".format(datetime.now()))
            return redirect('/')
        earned_gold = random.randint(-50,50)
        if earned_gold < 0:
            if session['gold'] - abs(earned_gold) > 0:
                print "{} - {} > 0".format(session['gold'], earned_gold)
                session['activity_list'].append("Entered a casino and lost {} gold... Ouch. ({})".format(abs(earned_gold), datetime.now()))
            else:
                session['activity_list'].append("Entered a casino and lost all of your gold... Ouch. ({})".format(datetime.now()))
                session['gold'] = 0
                return redirect('/')
        else:
            session['activity_list'].append("Entered a casino and earned {} gold. You got lucky! ({})".format(earned_gold, datetime.now()))
        session['gold'] += earned_gold
        return redirect('/')

    session['gold'] += earned_gold
    session['activity_list'].append("Earned {} gold from the {}! ({})".format(earned_gold, choice, datetime.now()))
    # print session['activity_list']
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session.pop('gold')
    session.pop('activity_list')
    return redirect('/')

app.run(debug=True)