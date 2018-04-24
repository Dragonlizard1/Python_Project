class Animal(object):
	def __init__(self, name1, health1):
		self.name = name1
		self.health = health1
		
		
	def walk(self):
		self.health -= 1

		return self

	def run(self):
		self.health -= 5

		return self

	def displayHealth(self):
		print self.health

		return self

class Dog(Animal):
	def __init__(self, name1):
		super(Dog, self).__init__(name1, 150)
		

	def pet(self):
		self.health +=5

		return self

class Dragon(Animal):
	def __init__(self, name1):
		super(Dragon, self).__init__(name1, 170)

	def fly(self):
		self.health -=10

		return self

	def displayDragon(self):
		self.displayHealth()
		print "I am a Dragon"

		return self

class newAnimal(object):
	def __init__(self, name1, heath1):
		self.name = name1
		self.health = health1



dog = Animal("doggie", 20)
dog.walk().walk().walk().run().run().displayHealth()
print "----"

dog1 = Dog("Bobby")
dog1.displayHealth()
dog1.walk().walk().walk().run().run().pet().displayHealth()
print "-----"

dragon1 = Dragon("Bob1")
dragon1.walk().run().fly().displayDragon()