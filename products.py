class Products(object):
	def __init__(self,name, price, link, description, quantity):
		self.name = name
		self.price = price
		self.link = link
		self.description = description
		self.quantity = quantity

	def add_product(self):
		pass

	
	def checkout(self,cart):
		#cart dict
		price = 0
		for item in cart:
			single = cart[item]
			price += single[1]
		return price


	def reduce_quantity(self, cart):
		pass

	def increase_quantity(self, qty):
		pass

	def get_quantity(self):
		pass

	def change_product_info(self):
		pass

