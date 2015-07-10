#defines a 'repeat' function that takes 2 argument
def repeat(s, exclaim):
	result = s * 3
	if  exclaim:
		result += '!!!'
	return result


def main():
	print repeat ('Yay', False)
	print repeat ('woo hoo', True)

print repeat('Yay', False)
print repeat('Woo Hoo', True)
