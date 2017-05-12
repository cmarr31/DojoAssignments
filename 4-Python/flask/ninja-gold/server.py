import random
from flask import Flask, render_template, redirect, request, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = "$2a$06$e/zKAwSoLSBfLP69mL7PA.odVryklj46O7m4Ppd8LOKJeepeKAn7a"

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
    earned_gold = 0
    if choice == "farm":
        earned_gold += random.randint(10,20)
        print "earned_gold", earned_gold
        session['gold'] += earned_gold
        session['activity_list'].append("Earned {} gold from the {}! ({})".format(earned_gold, choice, datetime.now()))
    elif choice == "cave":
        earned_gold += random.randint(5,10)
        print "earned_gold", earned_gold
        session['gold'] += earned_gold
        session['activity_list'].append("Earned {} gold from the {}! ({})".format(earned_gold, choice, datetime.now()))
    elif choice == "house":
        earned_gold += random.randint(2,5)
        print "earned_gold", earned_gold
        session['gold'] += earned_gold
        session['activity_list'].append("Earned {} gold from the {}! ({})".format(earned_gold, choice, datetime.now()))
    elif choice == "casino":
        if session['gold'] >= 50:
            earned_gold = random.randint(-50,50)
            print "earned_gold", earned_gold
            if earned_gold < 0:
                if session['gold'] - abs(earned_gold) <= 0:
                    session['gold'] = 0
                    session['activity_list'].append("Entered a casino and lost all of your gold... Ouch. ({})".format(datetime.now()))
                else:
                    print "{} - {} > 0".format(session['gold'], earned_gold)
                    session['gold'] += earned_gold
                    session['activity_list'].append("Entered a casino and lost {} golds... Ouch. ({})".format(abs(earned_gold), datetime.now()))
            else:
                session['gold'] += earned_gold
                session['activity_list'].append("Entered a casino and earned {} gold. You got lucky! ({})".format(earned_gold, datetime.now()))
        else:
            gold = session['gold']
            session['gold'] = session['gold']
            session['activity_list'].append("You need at least 50 golds to go to the casino! ({})".format(datetime.now()))
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session.pop('gold')
    session.pop('activity_list')
    return redirect('/')

app.run(debug=True)