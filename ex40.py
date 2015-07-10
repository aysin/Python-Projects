# practicing class (OOP)

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = ["Happy Birthday to you", 
		"I dont want to get sued",
		"So I will stip right there"]

bull_on_parade = Song(["They rally around tha family",
		"With pockets full of shells."])

#pass the variable happy_bday to the class to use instead
Song(happy_bday).sing_a_song()
#happy_bday.sing_a_song()
print ""
bull_on_parade.sing_a_song()