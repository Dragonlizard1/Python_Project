import random
coin = 5000

def coin_toss(num):
	head = 0
	tail = 0
	

	for count in range(1, num +1):
		x = random.random()
		x_rounded = round(x)
		if x_rounded == 0:
			head += 1
			print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(count, head, tail) 
		else:
			tail += 1
			print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(count, head, tail) 

	print "Ending the program, thank you!"

coin_toss(coin)
