givenlist1 = ['magical unicorns',19,'hello',98.98,'world']
givenlist2 = [2,3,1,7,4,12]
givenlist3 = ['magical','unicorns']

def whatisit(ylist):
	mixed = False
	listint = False
	liststr = False
	strlist = ""
	sumlist = 0

	for count in range(0,len(ylist),1):
		
		if (isinstance(ylist[count], int)) or (isinstance(ylist[count], float)):
			listint = True
			sumlist += ylist[count]
			if liststr == True:
				mixed = True
		else:
			liststr = True
			if count == 0:
				strlist = strlist + ylist[count]
			else:
				strlist = strlist + " " + ylist[count]
			if listint == True:
				mixed = True

	if mixed == True:
		print "The list you entered is of mixed type"
		print '"String: {}"'.format(strlist)
		print '"Sum: {}"'.format(sumlist)
	elif listint == True:
		print "The list you entered is of integer type"
		print '"Sum: {}"'.format(sumlist) 
	else:
		print "The list you entered is of string type"
		print '"String: {}"'.format(strlist)

whatisit(givenlist1)
print "-----"
whatisit(givenlist2)
print "-----"
whatisit(givenlist3)
