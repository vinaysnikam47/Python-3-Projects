# User will be asked if he wants to see next prime number
# If yes it will show next prime 


def is_prime(n):   # Function to check whether number is prime or not
    primes = [2]
    
    for x in range(3, n+1, 2):
        for y in range(3, n+1):
            if x % y != 0:
                continue
            else:
                if x == y:
                    primes.append(x)
                else:
                    break
                
    return n in primes


def main():  # Wrapping function
    num = 2
    
    while True:

        user_input = input('\nWould you like to see next prime number? Y/N ')
        if user_input.lower() == 'y':
            while True:
                if not is_prime(num):
                    num += 1
                    continue
                else:
                    print(num)
                    break
            num += 1      
            continue
        elif user_input.lower() == 'n':
            break
        else:
            print('Wrong input !')
            continue


if __name__ == '__main__':
    main()
