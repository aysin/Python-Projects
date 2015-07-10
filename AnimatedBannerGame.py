# "Animated Banner Game"
# UsingPython.com

import time
import os

# width of the display
width = 80

# message you wish to print
text = "hello!".upper()
printedText = ['', '', '', '', '', '', '']

#Dictinory mapping letters to their 7-line
chars = { " " : [' ',
				 ' ',
				 ' ',
				 ' ',
				 ' ',
				 ' ', 
				 ' '],
		  "E" : ['*****',
		  		 '*    ',
		  		 '*    ',
		  		 '*****',
		  		 '*    ',
		  		 '*    ',
		  		 '*****'],
		  "L" : ['*    ',
		  		 '*    ',
		  		 '*    ',
		  		 '*    ',
		  		 '*    ',
		  		 '*    ',
		  		 '*****'],
		  "H" : ['*   *',
		  		 '*   *',
		  		 '*   *',
		  		 '*****',
		  		 '*   *',
		  		 '*   *',
		  		 '*   *'],
		  "O" : ['*****',
		  		 '*   *',
		  		 '*   *',
		  		 '*   *',
		  		 '*   *',
		  		 '*   *',
		  		 '*****'],
		  "!" : ['  *  ',
		  		 '  *  ',
		  		 '  *  ',
		  		 '  *  ',
		  		 '  *  ',
		  		 '     ',
		  		 '  *  ']}
		  		 

# build up the printed banner
for row in range(7):
	for char in text:
		printedText[row] += (str(chars[char][row]) + ' ')

#the offset is how far the right we want to print the message
offset = width
while True:
	os.system('cls')

	# print each line of the text
	for row in range(7):
		print (" " * offset + printedText[row][max(0, offset *- 1): width - offset])

	# move the text to left
	offset -= 1
	if offset <= ((len(text) + 2) * 6) * -1:
		offset = width
	time.sleep(0.05)
















