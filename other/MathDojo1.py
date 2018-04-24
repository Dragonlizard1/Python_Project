class MathDojo(object):
	def __init__(self):
		self.result = 0
		self.resultcopy = 0		

	def add(self, *num):
		
		if isinstance(num, tuple):
			for element1 in num:
				
				self.result += element1
		else:
			self.result += num

		
		return self

	def subtract(self, *num):
		if isinstance(num, tuple):
			for element1 in num:			
				self.result -= element1
		else:
			self.result -= num
	
		return self
	

class MathDojo2(object):
	def __init__(self):
		
		self.resultcopy = 0		

	def add(self, *num):
		
		if isinstance(num, tuple):
			for element1 in num:
				if isinstance(element1, list):
					for element2 in element1:
						self.resultcopy += element2
				else:
					self.resultcopy += element1
		else:
			self.resultcopy += num

	
		return self

	def subtract(self, *num):
		if isinstance(num, tuple):
			for element1 in num:
				if isinstance(element1, list):
					for element2 in element1:
						self.resultcopy -= element2
				else:
					self.resultcopy -= element1
		else:
			self.resultcopy -= num
		
		return self
	


md = MathDojo()
md2 = MathDojo2()
print "part1"
print md.add(2,5).subtract(3,2).result
print "-----"
print "part 2"
print md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).resultcopy