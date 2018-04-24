testarr = [2, 4, 10, 16]
newarr = []
newarr2 = []
testarr1 = [2,4,5]

def layered_multiples(arr, multiples):
  new_arr1 = []
  for i in range(0, len(arr)):
  	layerarr = []

  	for count in range(0, arr[i]):

  		for count1 in range(0, multiples):
  			layerarr.append(1)
  	new_arr1.append(layerarr)

  return new_arr1


def multiply(arr, multiplier):
	arr = [2, 4, 10, 16]
	for i in range(0, len(arr)):
		arr[i] = arr[i] * multiplier
	
	return arr

def odd_even():

	for count in range(1,(2000 + 1)):
		if count%2 == 0:
			print "Number is {}. This is an even number.".format(count)
		else:
			print "Number is {}. This is an odd number.".format(count)
	

print "Odd and Even"	
odd_even()
print "-----"

print "Multiply the number in store array"
newarr = multiply(testarr, 5)	
print newarr
print "-----"

print "Layer multiples of 1"
newarr2 = layered_multiples(testarr1, 3)
print newarr2


