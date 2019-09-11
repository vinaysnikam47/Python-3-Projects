import requests


# Function for temperature conversion
def temp_converter():
    # Dictionary of formulae of temperature conversion
    conv_dic = {'cf': (lambda x: (x * (9 / 5) + 32)),
                'ck': (lambda x: (x + 273.15)),
                'fc': (lambda x: ((x - 32) * (5 / 9))),
                'fk': (lambda x: ((x - 32) * (5 / 9) + 273.15)),
                'kc': (lambda x: (x - 273.15)),
                'kf': (lambda x: ((x - 273.15) * (9 / 5) + 32)),
                'cc': (lambda x: x),
                'ff': (lambda x: x),
                'kk': (lambda x: x)}

    print('C >> Celsius\nK >> Kelvin\nF >> Fahrenheit')
    while True:
        try:
            conv_from = input("\nConvert from >> Choose C/K/F : ")
            conv_to = input("\nConvert to >> Choose from C/K/F: ")
            value = float(input("\nPlease enter value: "))

            conversion = conv_from.lower() + conv_to.lower()
            converted_value = round(conv_dic[conversion](value), 3)

            return print(f"{value} {conv_from.upper()} = {converted_value} {conv_to.upper()}")

        except:
            print('Wrong input !')
            continue


# Function for currency conversion
def currency_conv():
    # Url from which we get latest currency conversion in dictionary format of python
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()

    while True:
        try:
            print("\nThis currency values are based on USD.")
            conv_from = input("\nEnter currency you want to convert: ")
            conv_to = input("Enter currency to which you want to convert upper currency: ")
            value = float(input('\nPlease enter value: '))

            converted_value = (value * data['rates'][conv_to.upper()]) / data['rates'][conv_from.upper()]

            return print(f"{value} {conv_from.upper()} = {converted_value} {conv_to.upper()}")

        except:
            print('Wrong input !')
            continue


def main():  # Wrapping function

    print("\nWelcome to Temperature(T) and Currency(C) Converter !!")

    while True:

        user_input = input('\nWhich conversion you want to carry out T/C: ')

        if user_input.lower() == 't':
            temp_converter()
            break
        elif user_input.lower() == 'c':
            currency_conv()
            break
        else:
            print('Wrong input !')
            continue


if __name__ == '__main__':
    main()
