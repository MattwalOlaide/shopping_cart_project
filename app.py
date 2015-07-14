from flask import Flask, render_template, redirect, url_for, request, session, flash,Markup
from functools import wraps 
#from flask.ext.sqlalchemy import SQLALchemy

app = Flask(__name__)
app.secret_key = "aswa23ewd4rfeiu7"
#app.config.from_object('config'),instance_relative_config=True
#app.config.from_pyfile('config.py')
#db =  SQLALCHEMY(app)

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			message = Markup("<span class='error'>You need to log in to perform this action.</span>")
			flash(message)
			return redirect(url_for('login'))
	return wrap

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['email'] == 'me@you.com' and request.form['password'] == 'password':
			session['logged_in'] = True
			return redirect(url_for('shoes'))
			
			
		elif request.form['email'] == 'admin@feeton.com' and request.form['password'] == 'admin':
			session['logged_in'] = True
			return redirect(url_for('manage'))
		else:
			error = "Invalid username or password."
	return render_template('login.html', error = error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('home'))
	

@app.route('/reg')
def register():
	return render_template('register.html')

@app.route('/shoes')
@login_required
def shoes():
	return render_template('shoes.html')

@app.route('/manage')
@login_required
def manage():
	return render_template('mgt.html')



if __name__=='__main__':
	app.run(debug = True)
