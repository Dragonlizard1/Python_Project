class Product1(object):
	def __init__(self, price1, item_name1, weight1, brand1):
		self.price = price1
		self.item_name = item_name1
		self.weight = weight1
		self.brand = brand1
		self.status = "for sale"
		
	def display_all(self):
		print "Price:" , self.price
		print "Item:"  , self.item_name
		print "Weight:", self.weight
		print "Brand:" , self.brand
		print "Status:", self.status
		return self

	def change_status(self):
		if self.status == "for sale":
			self.status = "sold"
		return self

	def price_with_tax(self, tax):
		newprice = (self.price + (self.price * tax))
		return newprice

	def return_item(self, reason):
		if reason == "defective":
			self.price = 0
			self.status = "defective"
		elif reason == "box, like new":
			self.status = "for sale"
		else:
			if reason == "opened":
				self.status = "used"
				self.price = self.price - (self.price *.2)
		return self

prod = Product1(100, "X-BOX", "15lb", "Microsoft")
price = prod.price_with_tax(.08)
print "Price with tax: ",price
prod.return_item("defective")
prod.display_all()

def varargs(arg1, *args):
  print "Got "+arg1+" and "+ ", ".join(args)
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got o








