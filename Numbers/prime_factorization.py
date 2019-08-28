def prime_numbers(n): # Function to find out prime numbers
    primes = [2]
    for x in range(3,n+1,2):
        for y in range(3,n+1):
            if x%y != 0:
                continue
            else:
                if x == y:
                    primes.append(x)
                else:
                    break
    return primes

def main():  # Wrapping function
    while True:
        factors = []
        given_num = input("\nEnter a number to factorize or enter 'quit' to exit: ")
        if given_num.isdigit():
            num = int(given_num)
            prime_nums = prime_numbers(num)

            if num in prime_nums:
                print('Given number is prime number !')
                print(f'Factors of given numbers are: 1*{num}')
                continue
            elif num <= 0:
                print('Wrong Input!')
                continue
            else:
                i = 0    
                while prime_nums[i] <= num:
                    remainder = num%prime_nums[i]
                    if remainder == 0:
                        factors.append(prime_nums[i])
                        num = num/prime_nums[i]
                        continue
                    else:
                        i += 1
                        continue
                    break

            print(f'Factors of given numbers are: ',end = '')
            print('*'.join(str(number) for number in factors))
            continue
        else:
            if given_num == 'quit':
                break
            else:
                print('Wrong input!')
                continue
        
if __name__ == "__main__":
    main()
