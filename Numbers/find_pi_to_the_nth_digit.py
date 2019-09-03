# Pi value calculator
# Algorithm used - Chudnovsky algorithm

from math import *
from decimal import *

# Function to calculate iterated value of k
# K iteration calculates value of pi upto k-1 decimal
# So to find value of pi upto k we have to carry out k+1 iteration
def get_iterated_value_k(k): 

	k = k + 1
	value = 0
	getcontext().prec = k

	for k in range(k):

		numerator = factorial(6*k)*((545140134*k)+13591409)
		denominator = factorial(3*k)*((factorial(k))**3)*(262537412640768000**k)

		value += numerator/denominator

	return Decimal(value)

# Function to get value of Pi
def get_pi(k):

	iteration_value = get_iterated_value_k(k)
	up = Decimal(426880*sqrt(10005))

	pi = up/iteration_value

	return pi

# Wrapping function
def main():

	print("Welcome to Pi value calculator ! ")

	while True:

		k = input('\nEnter number of digits up to which you want to find value of Pi or enter quit to exit: ')

		if k == 'quit':
			break

		elif k.isdigit():
			n = int(k)
			print(get_pi(n))
			continue

		else:
			print("Wrong input!")
			continue


if __name__ == "__main__":
	main()




