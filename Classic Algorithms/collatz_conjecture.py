# Have the user enter a number greater than one
# If num is even divide by 2 
# If num is odd then multiply number by 3 and add 1 to it
# Program will tell number of steps reuires to reach 1


def collatz_recur(num):  # Function to find out number of steps

	count = 0

	while num != 1:
		if num % 2 == 0:
			num /= 2
			count += 1
			continue
		elif num % 2 != 0:
			num = (num*3) + 1
			count += 1
			continue
	return count


def main():  # Wrapping function

	while True:
		num = input("Enter a number or enter quit() to exit: ")
		if num.isdigit():
			if int(num) <= 1:
				print("Wrong input !")
				continue
			else:
				print(collatz_recur(int(num)))
				continue
		elif num == 'quit()':
			break
		else:
			print('Wrong input !')
			continue


if __name__ == "__main__":
	main()
