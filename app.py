import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, session, flash,Markup,jsonify
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import and_, select
#from api.user import new_user
#from .forms import LoginForm
from models import *


#import hashlib

#WTF_CSRF_ENABLED = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
app.secret_key = "aswa23ewd4rfeiu7"

app.config['UPLOAD_FOLDER'] = 'static/images/stock'

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


db =  SQLAlchemy(app)

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			message = Markup("<span class='error'> You need to log in to perform this action. </span>")
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
		form_email = request.form['email']
		form_password = request.form['password']
		
		user_info = Users.query.filter_by(user_email = form_email).first()
		
		if user_info is None:
			#"Invalid username or password. , user_password = form_password"
			error = "Invalid username or password. "
		else:
			if request.form['email'] == "admin@feeton.com":
				session['logged_in'] = True
				return redirect(url_for('manage'))
			session['logged_in'] = True
			return redirect(url_for('shoes'))
	return render_template('login.html', error = error)


@app.route('/login_open',methods=['GET','POST'])
def login_open():
	error = None
	return redirect(url_for('manage'), providers=app.config['OPENID_PROVIDERS'] )


	
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('home'))

count = 0
cart_dict = {}
@app.route('/keep_cart', methods=['GET','POST'])
def cart(item,price):
	
	cart_dict[count] = [item, price] 
	total_price += price
	count += 1
	return render_template('cart.html', cart = cart_dict, price = total_price)





@app.route('/upload', methods=['POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			now = datetime.now()
			filename = os.path.join(app.config['UPLOAD_FOLDER'], "%s.%s" % (now.strftime("%Y-%m-%d-%H-%M-%S-%f"), file.filename.rsplit('.', 1)[1]))
			file.save(filename)
			product_name = request.form['shoe_name']
			product_price = request.form['shoe_price']
			product_quantity = request.form['shoe_quantity']
			product_link = filename
			shoe_det = Products(product_name,product_price,product_quantity,product_link)
			db.session.add(shoe_det)
			db.session.commit()
			flash( 'One Stock Added.' )
		#return render_template('mgt.html')
		return jsonify({"success":True})

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/reg',methods=['GET','POST'])
def register():
	error = None
	if request.method == 'POST':
		new_user_email = request.form['email']
		new_user_password = request.form['password']
		if not new_user_email or not new_user_password:
			error = "Enter a valid email and password to register."
		chk_if_mail_exists = Users.query.filter_by(user_email = new_user_email).first()
		if chk_if_mail_exists:
			error = "Email already exists."
		else:
			user_reg = Users(new_user_email,new_user_password)
			db.session.add(user_reg)
			db.session.commit()
			flash('Registration successful.')
	return render_template('register.html',error = error)


@app.route('/checkout')
@login_required
def checkout():
	return render_template('checkout.html')


@app.route('/api/user',methods=['POST'])
def new_user():
	error = None
	user_email = request.form['email'] # request.json.get('email')
	user_password = request.form['password'] #request.json.get('password')
	if user_email is None or user_password is None:
		error = "Enter a valid email and password to register."
	if Users.query.filter_by(user_email = user_email).first() is None:
		error = "Email already exists."
	# user_reg = Users(user_email = user_email)
	# user_reg.hash_password(user_password)
		user_reg = Users(user_email, user_password)
		db.session.add(user_reg)
		db.session.commit()
		return jsonify({ 'user_email': user_email }),201,{ Location: url_for('shoes', id=user_id, _external=True )}
	return render_template('shoes.html',error = error)


@app.route('/shoes')
def shoes():
	#sh = Products.query.limit(9).all()
	#sh= "select * FROM Products"
	#print sh
	#shoes = {}
	# a_shoe = []
	# count = 0
	# temp = ""
	#for shoe in sh:
		#sh[1]
		# temp = shoe[0]
		#a_shoe.append(shoe[1])
		#a_shoe.append(shoe[2])
		#a_shoe.append(shoe[3])'''
	
		#shoes = sh
		# count += 1
	shoes ={
			'1':['shoe1.png', 35000, 10, 'Sneakers'],
			'2':['shoe1.png',45000,25,'cool sneaks'],
			'3':['shoe2.png',13000,10,'Nike 360']

	}

	return render_template('shoes.html', shoes = shoes)


@app.route('/manage')
#@login_required
def manage():
	return render_template('mgt.html')



if __name__=='__main__':
	app.run(debug = True)

'''
hashlib

	"shoeimage = shoe.png frm db"
	shoes ={
			'1':['shoe1.png', 35000, 10, 'Sneakers'],
			'2':['shoe1.png',45000,25,'cool sneaks'],
			'3':['shoe2.png',13000,10,'Nike 360']

	}
	'''