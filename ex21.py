def add(a, b):
	print "Adding %r and %r." %(a,b)
	return a + b

def subtract(a,b):
	print "Subtracting %r and %r." %(a,b)
	return a - b

def multiply(a, b):
	print "Multiplying %r and %r." %(a,b)
	return a * b

def divide(a,b):
	print "Divinding %r and %r." %(a,b)
	return a / b

print "Let's do some math with just functions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %r, Height: %r, Weight: %r, IQ: %r. " % (age, height, weight, iq)

print "\nHere is a puzzle"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"