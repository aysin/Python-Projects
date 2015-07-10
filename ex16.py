#Reading and writing to a file
from sys import argv

script, filename = argv
print "\nWe're goint to erase %r." %filename
print "If you dont want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("? >> ")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "\nNow Im going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

lines = line1 + '\n' + line2 + '\n' + line3
target.write(lines)

print "\nVery Good. Now Im going to show you what you have just recorded."
target = open(filename)
print target.read()


print "and Finally, we close the file."
target.close()