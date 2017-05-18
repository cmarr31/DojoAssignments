from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import os, binascii, md5
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
# Minimum 8 characters at least 1 Alphabet and 1 Number:
REGEX_PASSWORD = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

app = Flask(__name__)
app.secret_key = "WEGVEF11S12EGFE34SGS3WEG"
mysql = MySQLConnector(app, 'the_wall_db')

@app.route('/')
def login_page():
    return render_template('index.html')

@app.route('/register')
def registration_page():
    return render_template('register.html')

@app.route('/logout')
def log_out_user():
    session.clear()
    flash("Successfully logged out")
    return redirect('/')

@app.route('/the_wall')
def enter_wall():
    get_user_info_query = "SELECT * FROM users WHERE id = :id"
    get_user_info_data = { "id":session['current_user']}
    user = mysql.query_db(get_user_info_query, get_user_info_data)[0]
    session['first_name'] = user['first_name']
    get_messages_query = 'SELECT messages.id, CONCAT(first_name, " ", last_name) AS author, messages.content, DATE_FORMAT(messages.created_at, "%M %D %Y") AS date, messages.user_id FROM messages JOIN users ON (messages.user_id = users.id) ORDER BY messages.created_at DESC'
    retrieved_messages = mysql.query_db(get_messages_query)
    get_comments_query = 'SELECT comments.id, CONCAT(first_name, " ", last_name) AS author, comments.content, DATE_FORMAT(comments.created_at, "%M %D %Y") AS date, comments.user_id as user_id, comments.message_id as message_id FROM comments JOIN users ON (comments.user_id = users.id) ORDER BY comments.created_at'
    retrieved_comments = mysql.query_db(get_comments_query)
    return render_template("the_wall.html", messages=retrieved_messages, comments=retrieved_comments)

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
        return redirect('/the_wall')

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
    return redirect('/the_wall')

@app.route('/post_message/<user_id>', methods=["POST"])
def process_message_posted_by(user_id):
    message_content = request.form['message']
    insert_query = "INSERT INTO messages (content, created_at, updated_at, user_id) VALUES (:content, NOW(), NOW(), :user_id)"
    insert_data = { "content":message_content, "user_id":user_id }
    mysql.query_db(insert_query, insert_data)
    flash("Added new message to the database!")
    return redirect('/the_wall')

@app.route('/post_comment/<user_id>', methods=["POST"])
def process_comment_posted_by(user_id):
    message_id = request.form['message_id']
    comment_content = request.form['comment']
    insert_query = "INSERT INTO comments (content, created_at, updated_at, user_id, message_id) VALUES (:content, NOW(), NOW(), :user_id, :message_id)"
    insert_data = {"content":comment_content, "user_id":user_id, "message_id":message_id}
    mysql.query_db(insert_query, insert_data)
    flash("Added new comment to the database!")
    return redirect('/the_wall')

@app.route('/delete/<message_id>', methods=["POST"])
def delete_message(message_id):
    data = {"message_id":message_id, "user_id":session['current_user']}
    # Extra Credit I (optional) Allow the user to delete his/her own messages.
    # Extra Credit II (optional) Allow the user to delete his/her own message but only if the message was made in the last 30 minutes.
    delete_comments_query = "DELETE FROM comments WHERE created_at between date_add(NOW(),INTERVAL -30 MINUTE) and NOW()"
    delete_comments_query = delete_comments_query + " AND message_id = :message_id and user_id = :user_id"
    mysql.query_db(delete_comments_query, data)
    data = {"message_id":message_id, "user_id":session['current_user']}
    # Extra Credit I (optional) Allow the user to delete his/her own messages.
    # Extra Credit II (optional) Allow the user to delete his/her own message but only if the message was made in the last 30 minutes.
    delete_message_query = "DELETE FROM messages WHERE created_at between date_add(NOW(),INTERVAL -30 MINUTE) and NOW()"
    delete_message_query = delete_comments_query + " AND id = :message_id and user_id = :user_id"
    mysql.query_db(delete_message_query, data)
    return redirect('/the_wall')

@app.route('/delete_comment/<comment_id>')
def delete_comment(comment_id):
    data = {"comment_id":comment_id, "user_id":session['current_user']}
    # Extra Credit I (optional) Allow the user to delete his/her own messages.
    # Extra Credit II (optional) Allow the user to delete his/her own message but only if the message was made in the last 30 minutes.
    delete_comment_query = "DELETE FROM comments WHERE created_at between date_add(NOW(),INTERVAL -30 MINUTE) and NOW()"
    delete_comment_query = delete_comment_query + " AND id = :comment_id and user_id = :user_id"
    mysql.query_db(delete_comment_query, data)
    return redirect('/the_wall')

app.run(debug=True)