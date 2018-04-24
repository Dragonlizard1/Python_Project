sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def whatisit(whatis):
	if isinstance(whatis, int):
		if whatis >= 100:
			print "That's a big number!"
		else:
			print "That's a small number"	
	elif isinstance(whatis, basestring):
		if len(whatis) >= 50:
			print "Long sentence."
		else:
			print "Short sentence."
	else:
		if len(whatis) >= 10:
			print "Big list!"
		else:
			print "Short list."

whatisit(sI)
whatisit(mI)
whatisit(bI)
whatisit(eI)
whatisit(spI)
print "------"
whatisit(sS)
whatisit(mS)
whatisit(bS)
whatisit(eS)
print "------"
whatisit(aL)
whatisit(mL)
whatisit(lL)
whatisit(eL)
whatisit(spL)

