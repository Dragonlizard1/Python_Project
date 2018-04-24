class Bike(object):
	def __init__(self, price1, speed):
		self.price = price1
		self.max_speed = speed
		self.miles = 0

	def displayinfo(self):
		print "Price is:",self.price
		print "Max speed is:",self.max_speed
		print "Current miles is:", self.miles
		return self

	def ride(self):
		self.miles += 10
		return self

	def reverse(self):
		if self.miles > 0:
			self.miles -= 5  
		else:
			print "Cannot go reverse anymore"
		return self

bike1 = Bike(200, "25mph")
bike2 = Bike(200, "25mph")
bike3 = Bike(200, "25mph")
bike1.ride().ride().displayinfo()
print "------"
bike2.ride().ride().reverse().reverse().displayinfo()
print "------"
bike3.reverse().reverse().reverse().displayinfo()





"""
print user1.logged
print user1.email
"""

