from app import db

class Products(db.Model):
	__tablename__='products'
	product_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
	product_name = db.Column(db.String(120))
	product_price= db.Column(db.String(120))
	product_quantity = db.Column(db.Integer)
	product_description = db.Column(db.String(250))


	def __init__(self,name,price,quantity,description,link):
		self.product_name = name
		self.product_price = price
		self.product_quantity = quantity
		self.product_description = description
		self.product_link = link
		
	def __repr__(self):
		return '<name{}'.format(self.name)

