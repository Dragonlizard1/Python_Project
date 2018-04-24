def checkerboard():
	set1 = ""
	set2 = ""

	for count1 in range(0, 4):
		set1 += "*" + " "
	for count2 in range(0, 4):
		set2 += " " + "*"
	for count3 in range(0, 4):
		print set1
		print set2
	
checkerboard()




