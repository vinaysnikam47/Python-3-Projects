# Have the user enter a string
# Program will wheather string is palindrome or not 

def palindrome_check(string):  # Function to check for palindrome

	reversed_string = string[::-1]

	if string == reversed_string:
		return True

	else:
		return False


def main():  # Wrapping function
	while True:

		string = input("\nEnter a word to check for palindrome or enter quit() to exit: ")

		if string == 'quit()':
			break

		else:
			if palindrome_check(string):
				print("\nThis string is palindrome.")
				continue

			else:
				print("\nThis string is not palindrome.")
				continue

if __name__ == '__main__':
	main()


