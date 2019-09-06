# Have the user enter number of time coin to be flipped
# program will tell occurences, number of times we get head and number of time we get tails 

import random

# Function to get occurences and count
def coin_flips(num):

    occurences = []
    head = 0
    tail = 0

    for i in range(num):
        ran = random.choice(['H','T'])
        if ran == 'H':
            occurences.append('H')
            head += 1

        elif ran == 'T':
            occurences.append('T')
            tail += 1

    print(f'Occurences: {occurences}')
    print(f'Total number of heads: {head}')
    print(f'Total number of tails: {tail}')

# Wrapping function
def main():

    print('Welcome to Coin flip simulation !\nH >> Head\nT >> Tail')
    while True:

        number = input("\nEnter number of coin flips or enter quit to exit: ")

        if number == 'quit':
            break

        elif number.isdigit():
            num = int(number)
            coin_flips(num)

if __name__ == '__main__':
    main()




