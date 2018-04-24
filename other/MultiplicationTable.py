def rowsetting(multi):
	rowset = ""
	if multi == 0:
		multi = 1

	for count1 in range(1, 13):	
		num = count1 * multi	
		if count1 < 9:
			if len(str(num)) == 1:
				rowset += "  {}".format(str(num)) 
			else:
				rowset += " {}".format(str(num)) 
		else:
			if len(str(num)) == 1:
				rowset += "   {}".format(str(num)) 
			elif len(str(num)) == 2:
				rowset += "  {}".format(str(num))
			else:
			 	rowset += " {}".format(str(num))
	return rowset


def multiplicationTable():
	print "x " + rowsetting(0)

	for count in range(1,13):
		if len(str(count)) == 1:
			print str(count) + " " + rowsetting(count)
		else:
			print str(count) + rowsetting(count)
		
multiplicationTable()




