x = "There are %d types of people" %10
binary = "binary"
do_not = "don't"

y = "Those who know %s and those who %s." %(binary, do_not)

print x ,'\n', y
print "I said: %r." %x
print "I also said: %r." %y

hilarous  = False
joke_evaluation = "Isn't that joke funny? %r"
print joke_evaluation % hilarous 


w = "Aysin"
e = "Oruz"
print w + ' ' + e


#exercising printing with %r

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing.", "That you could type up right",
	"But it didnt sing.", "So I said goodnight.")

#printing exercise 
days = "Mon Tue Wed Thur Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJuly\nAug\nSep\nOct\nNov\nDec\n"

print "Here are the days: ", days
print "Here are the months: ", months 

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""


# exercising the qoutes and backslashes \t = tab key

tabby_cat = "\t Im tabbed in"
persian_cat = "I'm spliy \n on a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I will do a list:
\t * Cat food
\t * Fishes 
\t * Catnip\n\t * Grass
"""

print tabby_cat 
print persian_cat
print backslash_cat
print fat_cat





