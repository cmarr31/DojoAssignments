import os, binascii, md5
import re
from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector

# Minimum 8 characters at least 1 Alphabet and 1 Number:
REGEX_PASSWORD = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "BDF18690CCBC2FFEE2A756BC568A66FA"
mysql = MySQLConnector(app, 'login_and_registration_db')

@app.route('/')
def login_page():
    return render_template('index.html')

@app.route('/register')
def registration_page():
    return render_template('register.html')

@app.route('/logout', methods=['POST'])
def log_out_user():
    session.clear()
    flash("Successfully logged out")
    return redirect('/')

@app.route('/user_page')
def show_user_home_page():
    if 'current_user' in session.keys():
        get_user_info_query = "SELECT * FROM users WHERE id = :id"
        get_user_info_data = {'id':session['current_user']}
        current_user = mysql.query_db(get_user_info_query, get_user_info_data)[0]
        session['first_name'] = current_user['first_name']
        session['last_name'] = current_user['last_name']
        session['email'] = current_user['email']
    return render_template('user_page.html')

@app.route('/process_login', methods=["POST"])
def authenticate_login():
    email = request.form['email']
    password = request.form['password']
    failed_authentication = False
    check_email_exists_query = "SELECT email FROM users WHERE email = :email"
    check_email_data = {'email':email}
    email_check = mysql.query_db(check_email_exists_query, check_email_data)
    if len(email) < 1:
        flash("Email cannot be left blank!")
        failed_authentication = True
    elif not EMAIL_REGEX.match(email):
        flash("Please enter a valid email!")
        failed_authentication = True
    elif len(email_check) < 1:
        flash("No user found with this email address. Please register new user.")
        failed_authentication = True
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
        failed_authentication = True
    if failed_authentication:
        return redirect('/')
    get_user_info_query = "SELECT id, email, password, salt FROM users WHERE email = :email"
    get_user_info_data = {'email':email}
    user_info = mysql.query_db(get_user_info_query, get_user_info_data)[0]
    encrypted_password = md5.new(request.form['password'] + user_info['salt']).hexdigest()
    if user_info['password'] != encrypted_password:
        flash("Incorrect password! Please try again")
        failed_authentication = True
    if failed_authentication:
        return redirect('/')
    else:
        flash('Successfully logged in!')
        session['current_user'] = user_info['id']
        return redirect('/user_page')

@app.route('/process_registration', methods=["POST"])
def process_registration():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    salt = binascii.b2a_hex(os.urandom(15))
    encrypted_password = md5.new(request.form['password'] + salt).hexdigest()
    failed_validation = False
    if len(first_name) < 2:
        flash("First name must be at least 2 characters!")
        failed_validation = True
    elif not NAME_REGEX.match(first_name):
        flash("First name can only contain letters!")
        failed_validation = True
    if len(last_name) < 2:
        flash("Last name must be at least 2 characters!")
        failed_validation = True
    elif not NAME_REGEX.match(last_name):
        flash("Last name can only contain letters!")
        failed_validation = True
    check_email_exists_query = "SELECT email FROM users WHERE email = :email"
    check_email_data = {'email':email}
    email_check = mysql.query_db(check_email_exists_query, check_email_data)
    if len(email) < 1:
        flash("Email is required!")
        failed_validation = True
    elif not EMAIL_REGEX.match(email):
        flash("Please enter a valid email!")
        failed_validation = True
    elif len(email_check) > 0:
        flash("This email is already registered!")
        failed_validation = True
    if len(request.form['password']) < 1:
        flash("Password is required!")
        failed_validation = True
    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
        failed_validation = True
    elif request.form['confirm-password'] != request.form['password']:
        flash("Password confirmation failed")
        failed_validation = True
    if failed_validation:
        return redirect('/register')
    insert_query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :encrypted_password, :salt, NOW(), NOW())"
    insert_data = {
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'encrypted_password':encrypted_password,
        'salt':salt
    }
    mysql.query_db(insert_query, insert_data)
    flash("Successfully registered new user!")
    get_id_query = "SELECT id FROM users WHERE email = :email"
    get_id_data = {'email':email}
    session['current_user'] = mysql.query_db(get_id_query, get_id_data)[0]['id']
    return redirect('/user_page')

app.run(debug=True)