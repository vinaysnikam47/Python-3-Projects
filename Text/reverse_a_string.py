# Have user input string
# Program will return reversed string


def reverse_string(string):  # program to return reversed string

	return string[::-1]

def main():  # Wrapping function

	while True:  
		s = input("\nEnter a string to reverse it or enter quit() to exit: ")

		if s != 'quit()':
			print(f"\nReversed string : {reverse_string(s)}")
			continue

		else:
			break

if __name__ == "__main__":
	main()
