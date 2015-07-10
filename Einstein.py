#Einstein Game
#practice #1

print '''
First, write the number 1089 on a piece of paper, fold it, 
and hand it to a friend for safekeeping. 
What you wrote down is not to be read until 
you have completed your amazing mental feat. 
Next, ask your friend to write down any three-digit number,
emphasizing that the first and last digits must differ by at least two. 
Close your eyes or turn your back while this is being done. Better still,
have someone blindfold you.
'''

def reverse(num):
	return int(str(num)[::-1])

a = raw_input("Please enter three digit number, \nfirst and last digits must differ by at least two: ")
b = reverse(a)

print "Your number:", a, "\nReverse of your number:", b

if a > b:
	result = b - int(a) 
	print "Difference: ", result
else:
	result = int(a) - b 
	print "Difference: 1", result

print "Reverse of the difference:", reverse(result)
print "Result: ", int(result) + reverse(result)