# in this game you can type the color and not the word.. be careful :) 
# from usingpython.com

# import modules for creatin GUI 
from Tkinter import * 
import random 

# make a list of colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'White', 'Purple', 'Brown']

# keep track of the score
score = 0 
timeLeft = 30


#create a function that will start the game
def startGame(event):
	#if there is time...
	if timeLeft == 30:
		countdown()
	#run the funtion to choose color
	nextColor()

#display the colors
def nextColor():
	global score
	global timeLeft

	if timeLeft > 0:
		e.focus_set()

		if e.get().lower() == colors[1].lower():
			score += 1

		#clear the text entry
		e.delete(0, 'end')
		#shuffle the list of colors
		random.shuffle(colors)
		#change the color to type
		label.config(fg = str(colors[1]), text = str(colors[0]))
		#update the score
		scoreLabel.config(text = "Score: " + str(score))

# countdown timer
def countdown():
	global timeLeft

	if timeLeft > 0:
		#decement 
		timeLeft -= 1
		timeLabel.config(text = "Time Left: " + str(timeLeft))
		timeLabel.after(1000, countdown)

#create GUI window
root = Tk()
#Set the title
root.title("TTCANTW")
#set the size
root.geometry("375x200")

#add and instruction label
instruction = Label(root, text = "Type in the color of the words, and not the word text!", font = ('Helvetica', 12))
instruction.pack()

#add a score label
scoreLabel = Label(root, text = "Press enter to start", font = ('Helvetica', 12))
scoreLabel.pack()

#add a time left label
timeLabel = Label(root, text = "Time left: " + str(timeLeft), font = ("Helvetica", 12))
timeLabel.pack()

# add a label to displaying the colors
label = Label(root, font = ("Helvetica", 60))
label.pack()

#add a text entry box for typing
e = Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

#Start the GUI
root.mainloop()
























