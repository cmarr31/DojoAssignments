from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/name/<first_name>')
def name(first_name):
  return render_template('name.html', first_name=first_name)

@app.route('/process', methods=['POST'])
def create_user():
   first_name = request.form['first_name']
   print first_name
   return redirect('/name/' + first_name)
app.run(debug=True) 