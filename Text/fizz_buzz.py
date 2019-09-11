# FizzBuzz >> multiples of 3 and 5
# Fizz >> multiples of 3
# Buzz >> multiples of 5

if __name__ == "__main__":
    for num in range(1, 101):

        if num % 3 == 0 and num % 5 == 0:  # Numbers multiples of 3 and 5
            print("FizzBuzz")
        elif num % 3 == 0:  # Numbers multiple of 3
            print("Fizz")
        elif num % 5 == 0:  # Numbers multiple of 5
            print("Buzz")
        else:  # Other Numbers
            print(num)
