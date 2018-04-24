import random

def grade_score():
	scores = 0
	print "Scores and Grades"
	while scores < 10:
		grade = random.randint(59, 101)
		if (60 <= grade) and (grade <=69):
			scores += 1
			print "Score: {}; Your grade is D".format(grade)
		elif (70 <= grade) and (grade <=79):
			scores += 1
			print "Score: {}; Your grade is C".format(grade)
		elif (80 <= grade) and (grade <=89):
			scores += 1
			print "Score: {}; Your grade is B".format(grade)
		elif (90 <= grade) and (grade <=100):
			scores += 1
			print "Score: {}; Your grade is A".format(grade)
	print "End of the program. Bye!"


grade_score()
