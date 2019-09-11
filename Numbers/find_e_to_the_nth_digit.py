# Welcome to Euler's number e calculator !
# Have the user enter a digit
# Program will tell value of e upto that decimal


from math import factorial
from decimal import *


def get_e(n):  # Function to get value of e

	n = n + 1  # Otherwise this function will give value upto (n-1)th decimal
	getcontext().prec = n
	e = 0

	for i in range(50):
		e += Decimal(1/factorial(i))

	return e


def main():  # Wrapping function

	while True:
		user_input = input('\nEnter number of digits up to which you want to find value of e or enter quit to exit: ')

		if user_input == 'quit':
			break
		elif user_input.isdigit():
			n = int(user_input)
			print(f"Value of e: {get_e(n)}")
			continue
		else:
			print('Wrong input !')
			continue


if __name__ == '__main__':
	main()
