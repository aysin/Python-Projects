#creating list while doing loops

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for loop goes through a list

for n in the_count:
	print "This is count %d." % n

#same as above
for n in fruits:
	print "A fruit type is: %s." % n

for n in change:
	print "I got: %r." % n

#build an empty list
element = []

for n in range(0,6): 
	print "Adding %d to the list." % n
  	element.append(n)

for i in element:
	print "elements was: %d" % i