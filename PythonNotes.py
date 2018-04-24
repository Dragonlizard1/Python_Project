
andrew_rydzak
4:28 PM
var="andrEw"
var2=[1,2,1,4,1]
var3="an_drEw"
var4="-"
var5=["A","C","D"]
print(var.capitalize())
print(var.upper())
print(var.lower())
print(var2.count(1))
print(var.find("E"))
print(var3.split('d'))
print(var4.join(var5))
print(var3.replace('d','AAAAA'))
print("{} is a {}".format(var, var4))
vlist=[1,2,3,45,6,7]
olist=["Andrew","Billy"]

print(len(vlist))
print(max(vlist))
print(min(vlist))
print(vlist.index(45))
olist.append(23)
print(olist)
vlist.pop(3)
print(vlist)
vlist.remove(6)
print(vlist)
vlist.insert(0,"Drew")
print(vlist)
vlist.sort()
print(vlist)
vlist.reverse()
print(vlist)
vlist.extend(olist)
print(vlist)


#function 
def namefunction():
	print
	return;


str()   convert to string
int()    convert to integer
float()   convert to float


command prompt setting
cd desktop\codingdojo\python

dictionary setting with keys {} usage

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

for key in data.iterkeys():

for value in data.itervalue(): just value

for key, value in data.iteritems():
key and value

nested array
.keys()
.values()
.items()

zip(data1, data2) combine tuples
dict(data1) convert back to dictionary

import random
random.random()
random.randint(0,100)

this is for dictiony .then array inside

for key, data in context.items():
     #print data
     for value in data:
          print "Question #", value["id"], ": ", value["content"]
          print "----"

this is array then  dictionary is inside
students = [
     {'first_name' :  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def printlist1(arr):

	for data in arr:
		print "{} {}".format(data["first_name"], data["last_name"])
	


printlist1(students)

object OOP

class User(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):
        # set some instance variables. just like any variable we can call these anything
        self.name = name
        self.email = email
        self.logged = False
    # this is a method we created to help a user login
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
#now create an instance of the class
new_user = User("Anna","anna@anna.com")
print new_user.email

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Anna Propas", "anna@anna.com")
print user1.name
print user1.logged
print user1.email

for chaining method
user1.login().show().logout()

class Parent(object): # inherits from the object class
  # parent methods and attributes here
class Child(Parent):

print dic(modules)  # to show all the usage

class Parent1(object):
    def __init__(self):
        self.var1 = 1

class Parent2(object):
    def _init__(self):
        self.var2 = 2

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)

----


        structure time  
        website  https://docs.python.org/2/library/time.html
import time
from time import strftime, localtime
strftime("%I:%M")

----
sorted specific nested array
 sorted(student_tuples, key=lambda student: student[2])

class sorting  array inside a tuple calls[].call.time
  self.calls = sorted(self.calls, key=lambda call:call.time)

  ---------
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
        ]
print sorted(student_tuples, key=lambda student: student[2])
#print student_tuples
