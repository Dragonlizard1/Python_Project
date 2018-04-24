list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_one1 = [1,2,5,6,5]
list_two1 = [1,2,5,6,5,3]

list_one2 = [1,2,5,6,5,16]
list_two2 = [1,2,5,6,5]

list_one3 = ['celery','carrots','bread','milk']
list_two3 = ['celery','carrots','bread','cream']

def compareit(xlist, ylist):
	if xlist == ylist:
		print "The lists are the same"
	else:
		print "The lists are not the same"

compareit(list_one, list_two)
print "-----"
compareit(list_one1, list_two1)
print "-----"
compareit(list_one2, list_two2)
print "-----"
compareit(list_one3, list_two3)

