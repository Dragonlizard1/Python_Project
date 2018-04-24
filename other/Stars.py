x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(arrstar):
	addstar = ""
	for i in range(0, len(arrstar)):
		addstar = ""
		for count in range(0, arrstar[i]):	
			addstar += "*"
		print addstar

def draw_stars2(arrstar1):   #mixed and print special char
	addstar = ""
	for i in range(0, len(arrstar1)):
		addstar = ""

		if isinstance(arrstar1[i], basestring):
			string1 = arrstar1[i]
			char1 = string1[0].lower()
			for count in range(0, len(string1)):	
				addstar += char1
		else:
			for count in range(0, arrstar1[i]):	
				addstar += "*"
		print addstar

print "number in array"
draw_stars(x)

print "--------"
print "number and string in array as string first char as a char print"
draw_stars2(y)
