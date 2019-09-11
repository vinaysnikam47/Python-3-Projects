# Have the user enter a number
# Program will tell its factorial


def factorial(num):  # Function to find out factorial

	fact = 1

	if num == 0:
		print(f"\nFactorial of {num} : {fact}")
	else:
		for i in range(num, 1, -1):
			fact *= i
		print(f"\nFactorial of {num} : {fact}")


while True:  # Wrapping function

	user_input = input("\nEnter a number to get its factorial or enter quit() to exit: ")

	if user_input == 'quit()':
		break
	elif user_input.isdigit():
		num = int(user_input)
		factorial(num)
		continue
	else:
		print("\nWrong input !")
		continue
