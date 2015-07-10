#Doing game 

from sys import argv
from sys import exit

#name = argv
name = raw_input('\nPlease enter your name: ')
print '\nWelcome come to the game', name,', The Room!'
print 'You are in a building and there are 5 rooms.'
print 'Your mission is to reach to the treasure.'
print 'Your only way to reach to the treasure is to find the correct room,'
print 'defeat the obstacle and get the treasure, You win!'
print 'Here are the rooms.. Please enter the room number: '
print '1. The Cockatrice Room'
print '2. The Bear Room'
print '3. Star Wars Room'
print '4. TV Room'


def bear_room():
	print 'Welome to the Bear Room.'
	print 'There is a bear holding a cake and honey. You need to pass the bear.'
	print 'What would you do?\n1. Take away the honey. \n2. Take away the cake.'
	print '3. Cry. '

def cockatrice():
	pass

def star_wars():
	pass

def tv():
	pass