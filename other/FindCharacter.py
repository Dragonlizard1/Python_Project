word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def findit(xlist, findchar):
	newarr = []
	for count in range(0, len(xlist)):
		if xlist[count].find("o") > 0:
			newarr.append(xlist[count])
	print "new_list = {}".format(newarr)
	

findit(word_list, char)




