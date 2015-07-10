#exercise 19 - Learn Python the hard way
#Functions and variables

def cheese_and_crackers(cheese_count, cracker_count):
	print "You have %d cheeses!" %cheese_count
	print "You have %r crackers!" %cracker_count
	print "Enough for the party"

def drinks(wine, beer):
	print "You have %r beers " %beer
	print "You have %r bottle of wine." %wine


print "You can just give the function numbers directly"
cheese_and_crackers(20,50)
drinks(12, 20)

print "You can use variables from out script: "
cheese = 10
cracker = 30
cheese_and_crackers(cheese, cracker)


#Functions and files

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines"
current_line = 1

for current_line in range(1,4):
	print_a_line(current_line, current_file)





