#working on while loop

#create a variable and assign it to 0
#create a empty list

def whileFunction(a):
	i = 0
	numbers = []

	while i < a:
		print "At the top i is %d" %i
		numbers.append(i)

		i += 2
		print "numbers now: ", numbers
		print "At the bottom i is %d" %i

	print "The numbers: "
	for n in numbers:
		print n


print whileFunction(8)