import time
from time import strftime, localtime


class Call(object):
	def __init__(self, id1, name, phone, time, reason):
		self.id1 = id1
		self.name = name
		self.phone = phone
		self.time = time
		self.reason = reason

	def display(self):
		print self.id1
		print self.name
		print self.phone
		print self.time
		print self.reason

		return self

class CallCenter(object):
	def __init__(self, id1, name, phone, time, reason):
		
		self.calls = [Call(id1, name, phone, time, reason)]
		self.queue = 0

	def addcall(self, id1, name, phone, time, reason):
		self.calls.append(Call(id1, name, phone, time, reason))	
		self.queue = len(self.calls)

		return self

	def removecall(self, pos):

		self.calls.pop(pos)
		self.queue = len(self.calls)

		return self

	def info(self):
		for element in self.calls:
			print "Name:", element.name
			print "Phone Number:", element.phone
			print "There is {} queue:".format(self.queue)
			print ""

	def find_number(self, num):
		for i in range(len(self.calls)):
			if num == self.calls[i].phone:
				self.removecall(i)
				break

	def sorting(self):
		 self.calls = sorted(self.calls, key=lambda call:call.time)
	

		 return self

#strftime("%I:%M")  structure time if need to be implemented in real time.

Baylor = CallCenter("1", "Bob", 46343, "11:31","addin")
Baylor.addcall("2", "jacob", 423423443, "10:28","adding again")
Baylor.addcall("3", "David", 9419431, "09:30","adding 2 again")

Baylor.sorting()   #sort the time

print "---"
Baylor.info()
