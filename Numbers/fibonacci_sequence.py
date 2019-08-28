# Fibonacci sequence program upto user given number

def fibonacci_sequence(n):  # Function to find out fibonacci sequence
    x = 1
    y = 1
    for i in range(100):
        yield x
        x,y = y, x+y
        
        
def main():   # Wrapping function
    while True: 
        fibonacci_sequence_list = []
        user_input = input('\nEnter number upto which you want fibonacci sequence or enter quit to exit: ')

        if user_input.isdigit():
            number = int(user_input)
            for num in fibonacci_sequence(number):
                if num < number:
                    fibonacci_sequence_list.append(num)
            print(fibonacci_sequence_list)
            continue
        elif user_input == 'quit':
            break
        else:
            print('Wrong input !')
            continue
    
if __name__ == '__main__':
    main()
