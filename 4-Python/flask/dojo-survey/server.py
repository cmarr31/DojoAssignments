# dojo-survey
from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "dojo"

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process_validation():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    error = False
    if len(session['name']) < 1:
        flash("Name is a required field")
        error = True
    if len(session['comment']) < 1:
        flash("Comment is a required field")
        error = True
    if len(session['comment']) > 120:
        flash("Comment cannot be longer than 120 characters!")
        error = True
    if error == True:
        return redirect('/')
    else:
        return render_template('result.html')
app.run(debug=True)