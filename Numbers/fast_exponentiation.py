# Have the user enter number and power
# Program will tell the number^power

def main():

	while True:

		num = int(input("\nEnter number: "))
		power = int(input('Enter power: '))

		answer = num**power
		print(f'\n{num} to the power of {power} is equal to ({num}^{power}): {answer}')

if __name__ == '__main__':
	main()

