x = {"name":"Anna","age":101, "country":"The United States", "favorite":"Python"}

def dictionary_print(xdic):
	print "My name is {}".format(xdic["name"])
	print "My age is {}".format(xdic["age"])
	print "My country of birth is {}".format(xdic["country"])
	print "My favorite language is {}".format(xdic["favorite"])

def dictionary_item(xdic):
	print "key and values"
	print xdic.items()
	print "-----"

	print "key of dictionary"
	print xdic.keys()
	print "-----"

	print "values of dictionary"
	print xdic.values()

dictionary_print(x)
print "-----"
dictionary_item(x)
