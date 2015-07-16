from app import db
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


class Users(db.Model):
	__tablename__= 'users'
	user_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
	user_email = db.Column(db.String(120))
	user_password = db.Column(db.String(120))

	def __init__(self,email,password):
		self.user_email = email
		self.user_password = password

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(self.password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)


	def generate_auth_token(self, expiration=600):
		s = Serializer(app.config['SECURITY_KEY'], expires_in = expiration )
		return s.dumps({'id':self.id})


	@staticmethod
	def verify_auth_token(token):
		s = Serializer(app.config['SECURITY_KEY'])
		try:
			data = s.loads(token)
		except SignatureExpired:
			return None #Code valid but expired
		except BadSignature:
			return None
		user = User.query.get(data['id'])
		return user



class Products(db.Model):
	__tablename__= 'products'
	product_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
	product_name = db.Column(db.String(120))
	product_price= db.Column(db.String(120))
	product_quantity = db.Column(db.Integer )
	product_link = db.Column(db.String(250))

	def __init__(self,name,price,quantity,link):
		self.product_name = name
		self.product_price = price
		self.product_quantity = quantity
		#self.product_description = description
		self.product_link = link
		
	