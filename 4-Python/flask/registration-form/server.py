import re, time
from flask import Flask, render_template, redirect, request, session, flash
from datetime import datetime

REGEX_EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Minimum 8 characters at least 1 Alphabet and 1 Number:
REGEX_PASSWORD = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

app = Flask(__name__)
app.secret_key = "dojo"

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process_validation():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['password_confirm'] = request.form['password_confirm']
    session['birthday'] = request.form['birthday']
    validation_failed = False

    if len(session['first_name']) < 1:
        flash("First name is required!", 'error')
        validation_failed = True
    else:
        if not session['first_name'].isalpha():
            flash("First name can only include alphabetical characters!", 'error')
            validation_failed = True

    if len(session['last_name']) < 1:
        flash("Last name is required!", 'error')
        validation_failed = True
    else:
        if not session['last_name'].isalpha():
            flash("Last name can only include alphabetical characters!", 'error')
            validation_failed = True

    # Add a birth-date field that must be validated as a valid date and must be from the past.
    birthday = datetime.strptime(session['birthday'], '%m/%d/%Y')
    now = datetime.now()
    print "convert {} > {}".format(birthday, now)
    if len(session['birthday']) < 1:
        flash("Birthday is required!", 'error')
        validation_failed = True
    elif birthday >= now:
        flash("Birthday must be from the past!", 'error')
        validation_failed = True
        print "error {} > {}".format(birthday, now)
    else:
        print "ok {} and {}".format(birthday, now)

    if len(session['email']) < 1:
        flash("Email is required!", 'error')
        validation_failed = True
    elif not REGEX_EMAIL.match(session['email']):
        flash("Please enter a valid email", 'error')
        validation_failed = True

    # Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value.
    if len(session['password']) < 1:
        flash("Password is required!", 'error')
        validation_failed = True
    elif not REGEX_PASSWORD.match(session['password']):
        flash("Password must be at least 8 characters with at least 1 uppercase letter and 1 numeric value!", 'error')
        validation_failed = True

    if len(session['password_confirm']) < 1 or session['password_confirm'] != session['password']:
        flash("Password confirmation must match!", 'error')
        validation_failed = True

    if validation_failed == False:
        flash("Success!", 'success')

    return redirect('/')

app.run(debug=True)