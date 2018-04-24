
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

"""
command prompt setting
cd desktop\codingdojo\python

dictionary setting with keys {} usage

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

"""
