# Have the user enter a credit card number
# Program will tell whether it is valid credit card number
# Algorithm used - https://www.sapling.com/7966257/checksum-credit-card

def multi_2_array(number):

    list_of_15_digits = list(number[:-1])

    list_of_15_digits_int = [int(num) for num in list_of_15_digits]

    list_aft_multi_2 = []

    for i in range(len(list_of_15_digits_int)):

        if i % 2 == 0:
            list_aft_multi_2.append(list_of_15_digits_int[i]*2)

        else:
            list_aft_multi_2.append(list_of_15_digits_int[i])

    return list_aft_multi_2


def sum_calculator(lst):

    list_after_addition = []

    for num in lst:

        if num > 9:
            in_str = str(num)
            multiplied_number = int(in_str[0])+int(in_str[1])

            list_after_addition.append(multiplied_number)

        else:
            list_after_addition.append(num)

    return sum(list_after_addition)


def main():

    while True:

        number = input("\nEnter 16 digits credit card number to be checked for validation: ")

        if len(number) == 16:

            check_digit = int(number[-1])

            array = multi_2_array(number)

            sum_of_15_digits = sum_calculator(array)

            if (sum_of_15_digits + check_digit) % 10 == 0:

                print(f"\n{number[:4]} {number[4:8]} {number[8:12]} {number[12:]} is valid Credit Card number.")
                break

            else:
                print(f"\n{number[:4]} {number[4:8]} {number[8:12]} {number[12:]} is not valid Credit Card number.")
                break

        else:
            print("\nSomething's wrong ! Have you entered 16 digit credit card number?")
            continue


if __name__ == "__main__":
    while True:
        try:
            main()
            break
        except:
            print("\nSomething's wrong! Please try again !" )
            continue
