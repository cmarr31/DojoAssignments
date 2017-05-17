from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re

# Minimum 8 characters at least 1 Alphabet and 1 Number:
REGEX_PASSWORD = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "super awesome secret key"
mysql = MySQLConnector(app, 'email_validation')

@app.route('/')
def enter_email_page():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def validation_check():
    email = request.form['email']

    if len(email) < 1:
        flash("Email cannot be left blank!")
    elif EMAIL_REGEX.match(email):
        print "Inserting into database"
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {'email':email}
        mysql.query_db(query, data)
        flash("The email address you entered (" + email + ") is a VALID email address! Thank you!")
        return redirect('/emails')
    else:
        flash("Please Enter a Valid Email Address!")
    return redirect('/')

@app.route('/emails')
def display_email_list():
    emails = mysql.query_db("SELECT id, email, DATE_FORMAT(created_at, '%m/%d/%Y %l:%i %p') as created_at  from emails")
    # print emails
    return render_template('emails.html', all_emails=emails)

@app.route('/emails/<email_id>/delete', methods=['POST'])
def delete_email(email_id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id':email_id}
    mysql.query_db(query, data)
    return redirect('/emails')

app.run(debug=True)