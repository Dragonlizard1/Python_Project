class Product1(object):
	def __init__(self, price1, item_name1, weight1, brand1):
		self.price = price1
		self.item_name = item_name1
		self.weight = weight1
		self.brand = brand1
		self.status = "for sale"

print Product1().status