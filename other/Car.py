class Car(object):
	def __init__(self, price1, speed1, fuel1, mileage1):
		self.price = price1
		self.speed = speed1
		self.fuel = fuel1
		self.mileage = mileage1

		if price1 > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()

	def display_all(self):
		print "Price:",self.price
		print "Speed:",self.speed
		print "Fuel:", self.fuel
		print "Mileage:", self.mileage
		print "Tax:", self.tax
		return self


Car(2000, "35mph", "Full", "15mpg")
print "-----"
Car(2000, "5mph", "Not Full", "105mpg")
print "-----"
Car(2000, "15mph", "Kind of Full", "95mpg")
print "-----"
Car(2000, "25mph", "Full", "25mpg")
print "-----"
Car(2000, "45mph", "Empty", "25mpg")
print "-----"
Car(20000000, "35mph", "Empty", "15mpg")




