# Have the user enter a string
# program will tell total no. of vowels also count of each vowel


def vowel_count(string):  # Function to count vowels

    vowels = ['a', 'e', 'i', 'o', 'u']

    count = 0
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for letter in string:
        if letter in vowels:
            count += 1
            if letter == 'a':
                a += 1
            elif letter == 'e':
                e += 1
            elif letter == 'i':
                i += 1
            elif letter == 'o':
                o += 1
            elif letter == 'u':
                u += 1

    return count, a, e, i, o, u


def main():  # Wrapping function
    while True:

        string = input("\nEnter a string to count vowels or enter quit() to exit: ")

        if string == 'quit()':
            break
        else:
            count_tuple = vowel_count(string)

            print(f"\nTotal Vowels: {count_tuple[0]}")
            print(f"Count of a : {count_tuple[1]}")
            print(f"Count of e : {count_tuple[2]}")
            print(f"Count of i : {count_tuple[3]}")
            print(f"Count of o : {count_tuple[4]}")
            print(f"Count of u : {count_tuple[5]}")
            continue


if __name__ == '__main__':
    main()
