#functions

#this one is like scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "Arg1: %r, arg2: %r." % (arg1, arg2)

#better one is this
def print_two_again(arg1, arg2):
	print "Arg1: %r, arg2: %r." %(arg1, arg2)

#takes one argument 
def print_one(arg):
	print "Arg: %r" %arg

def print_none():
	print "I got nothing."

print_two("Aysin", "oruz")
print_two_again("Aysin", "Oruz")
print_one("Gotcha")
print_none()