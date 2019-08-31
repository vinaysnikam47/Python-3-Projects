# Have the user enter a word
# Program will return its pig latin form 


def pig_latin(string):  # Function to get pig latin form

	vowels = ['a','e','i','o','u'] 

	if string[0] in vowels:
		print(f"\nPig latin form of '{string}' : {string+'way'}")

	elif string[1] in vowels:
		print(f"\nPig latin form of '{string}' : {string[1:] + string[0] + 'ay'} ")

	else:
		for j in range(len(string)-1):
			if string[j] in vowels:
				break

		print(f"\nPig latin form of '{string}' : {string[j:] + string[:j] + 'ay'}")


def main():  # Wrappng function
	while True:  

		string = input('\nEnter a word to get its pig latin form or enter quit() to exit: ')

		if string != 'quit()':
			pig_latin(string)
			continue

		else:
			break

if __name__ == '__main__':
	main()




