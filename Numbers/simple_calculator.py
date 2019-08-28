# Simple calculator which makes addition, subtraction, multiplication, division
# '+' = addition
# '-' = subtraction
# '*' = multiplication
# '/' = division


def main():    # main function which makes opertions on user given numbers
    while True:
        num1 = float(input('Enter first number: '))
        num2 = float(input('\nEnter second number: '))
        operation = input("\nWhich operation would you like to do? Choose between ['+','-','*','/']: ")

        if operation == '+':
            addition = num1 + num2
            print(f'\n{num1} + {num2} = {addition}')

        elif operation == '-':
            subtraction = num1 - num2
            print(f'\n{num1} - {num2} = {subtraction}')

        elif operation == '*':
            multiplication = num1*num2
            print(f'\n{num1} * {num2} = {multiplication}')

        elif operation == '/':
            division = num1/num2
            print(f'\n{num1} / {num2} = {division:{4}.{4}}')

        else:
            print('\nWrong input !')
            continue
        break
            
def sub_main():    # Function to ask whether to make next operation or not
    while True: 
        user_input = input('\nWould you like to make another operation? Y/N ')

        if user_input.lower() == 'y':
            main()
        elif user_input.lower() == 'n':
            break
        else:
            print('Wrong input !')
            continue      


if __name__ == '__main__':
    while True:
        try:
            main()
            sub_main()
            break
        except:
            print('wrong input !')
            continue
        
