students = [
     {'first_name' :  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printlist1(arr):

	for data in arr:
		print "{} {}".format(data["first_name"], data["last_name"])
	
def printlist2(xdic):
	count = 1
	for key, data in xdic.items():
		print key

		for value in data:
			length1 = len(value["first_name"]) + len(value["last_name"])
			print "{} - {} {} - {}".format(count, value["first_name"].upper(), value["last_name"].upper(), length1)

print "Array with dictionary"
print "-----"
printlist1(students)
print "-----"

print "Dictionary with array"
print "-----"
printlist2(users)



