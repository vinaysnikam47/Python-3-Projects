# Have the user enter a number below 1000000
# Program will tell its name

# Function to find out names of number upto 99
def below_100(number):

	name = ''
	s = str(number)
	list_num = [int(n) for n in s] + [' ']

	if number <= 19:
		name += first_nineteen[number].capitalize()
		return name

	else:
		tenth_place = list_num[-3]
		ones = list_num[-2]

		name += (tens[tenth_place].capitalize() + ' ' + first_nineteen[ones])
		return name

# Function to find out names of number from 100 to 999
def below_1000(number):

	name = ''
	s = str(number)
	list_num = [int(n) for n in s] + [' ']
	hundredth_place = list_num[-4]
	tenth_place = list_num[-3]
	ones = list_num[-2]

	name += (first_nineteen[hundredth_place].capitalize() + ' ' + places[1])

	if number%100 == 0:
		return name
		
	elif number%100 <= 19:
		name += (' and ' + first_nineteen[number%100]) 
		return name

	else:
		name += (' and ' + tens[tenth_place].capitalize() + ' ' + first_nineteen[ones])
		return name

# Function to find out names of number from 1000 to 999999
def below_100000(number):

	name = ''
	s = str(number)
	list_num = [int(n) for n in s] + [' ']
	thousand_place = list_num[-5]
	hundredth_place = list_num[-4]
	tenth_place = list_num[-3]
	ones = list_num[-2]

	name += (below_100(number//1000) + ' ' + places[2])

	if number % 1000 == 0:
		return name

	elif number % 1000 < 100:
		reamining = below_100(number%1000)
		name += (' ' + reamining)
		return name

	else:
		reamining = below_1000(number%1000)
		name += (', ' + reamining)
		return name

def below_1000000(number):

	name = ''
	s = str(number)
	list_num = [int(n) for n in s] + [' ']
	thousand_place = list_num[-5]
	hundredth_place = list_num[-4]
	tenth_place = list_num[-3]
	ones = list_num[-2]

	name += (below_1000(number//1000) + ' ' + places[2])

	if number % 1000 == 0:
		return name

	elif number % 1000 < 100:
		reamining = below_100(number%1000)
		name += (' ' + reamining)
		return name

	else:
		reamining = below_1000(number%1000)
		name += (', ' + reamining)
		return name

# Function to assemble upper functions
def main():

	while True:

		if number < 100:
			print(below_100(number))
			break

		elif number < 1000:
			print(below_1000(number))
			break

		elif number < 100000:
			print(below_100000(number))
			break

		elif number < 1000000:
			print(below_1000000(number))
			break


if __name__ == '__main__':
	while True:
		num = input("\nEnter a number: ")

		number = int(num)

		first_nineteen = ['','one','two','three','four','five','six','seven','eight','nine'\
		,'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']

		tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

		places = ['','hundred','thousand']
		
		main()
