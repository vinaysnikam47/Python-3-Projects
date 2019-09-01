# Have the user enter a number
# Program will tell its factorial

def factorial(num):  # Function to find out factorial

	factorial = 1

	if num == 0:
		print(f"\nFactorial of {num} : {factorial}")
	else:
		for i in range(num,1,-1):
			factorial *= i
		print(f"\nFactorial of {num} : {factorial}")


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
