# making decision Exercise 31

print "You enter a dar room with two doors.\nDo you go through door #1 or door #2?"

door = raw_input('> ')

if door == "1" :
	print "There is a giant bear hee earing a cheese cake. What you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input('> ')
	if bear == '1': 
		print "The bear eays your face off. Good job!"
	elif bear == '2':
		print "The bear eats your legs off. Good job!"
	else:
		print "Yeah, doin %r sound like a better idea!" %bear
		
if door == '2':
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input('> ')
	if insanity == '1' or insanity == '2':
		print "Your body survivess powered by a mind of jello. Good job!"
	else: 
		print "The insanity rots your eyes into a pool of muck. Good Job!"		
else:
	print "You stumble around and fall on a knife and die. Good job!"
