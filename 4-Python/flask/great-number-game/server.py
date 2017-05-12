import random
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "dojo"

@app.route('/')
def home():
    if 'number' not in session.keys():
        session['number'] = random.randint(1,10)
        session['phrase'] = "Take a guess!"
        session['color'] = "blue"
    if 'guess' in session.keys():
        if session['guess'] > session['number']:
            session['phrase'] = "Too high! Guess a lower number"
            session['color'] = "red"
        elif session['guess'] < session['number']:
            session['phrase'] = "Too low! Guess a higher number"
            session['color'] = "yellow"
        else:
            session['phrase'] = str(session['number']) + " was the number!"
            session['color'] = "green"
    print "HOME: ", session
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    print "Getting guess"
    session['guess'] = int(request.form['guess'])
    print session['guess']
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('guess')
    session.pop('number')
    session.pop('color')
    session.pop('phrase')
    print session
    return redirect('/')

app.run(debug=True)