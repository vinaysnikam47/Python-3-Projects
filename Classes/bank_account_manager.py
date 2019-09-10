# Bank Account Manager

# Class for Checking Account


class CheckingAccount:

    def __init__(self, pin, owner, balance):
        self.pin = pin
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amount):
        self.balance += dep_amount
        print(f'Deposit Successful ! Your new balance is ₹{self.balance}')

    def withdrawl(self, with_amount):
        if with_amount > self.balance:
            print('Sorry ! You do not have enough balance !')
            print(f'You have ₹{self.balance} in your account')
        else:
            self.balance -= with_amount
            print(f'Withdrawl Successful ! Your new balance is ₹{self.balance}.')

    def show_balance(self):
        print(f'Your balance is ₹{self.balance}')

# Class for Saving Account


class SavingAccount:

    def __init__(self, pin, owner, balance):
        self.pin = pin
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amount):
        self.balance += dep_amount
        print(f'Deposit Successful ! Your new balance is ₹{self.balance}')

    def withdrawl(self, with_amount):
        if with_amount > self.balance:
            print('Sorry ! You do not have enough balance !')
            print(f'You have ₹{self.balance} in your account')
        else:
            self.balance -= with_amount
            print(f'Withdrawl Successful ! Your new balance is ₹{self.balance}.')

    def show_balance(self):
        print(f'Your balance is ₹{self.balance}')

# Class for Business Account


class BusinessAccount:

    def __init__(self, pin, owner, balance):
        self.pin = pin
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amount):
        self.balance += dep_amount
        print(f'Deposit Successful ! Your new balance is ₹{self.balance}')

    def withdrawl(self, with_amount):
        if with_amount > self.balance:
            print('Sorry ! You do not have enough balance !')
            print(f'You have ₹{self.balance} in your account')
        else:
            self.balance -= with_amount
            print(f'Withdrawl Successful ! Your new balance is ₹{self.balance}.')

    def show_balance(self):
        print(f'Your balance is ₹{self.balance}')

# Function for ATM operation


def atm_operation(pin):
    while True:
        acc_type = {'1': 'Checking', '2': 'Saving', '3': 'Business'}
        print('\n1. Checking Account\n2. Saving Account\n3. Business Account\n4. Exit')
        select_acc = input('\nPlease select Account type: ')
        if select_acc in acc_type.keys():
            if acc_type[select_acc] in account_dic[pin]['Acc_type'].keys():
                print('\n1. Show Balance\n2. Withdraw Amount\n3. Deposit Amount\n4. Exit ')
                user_input = input('\nEnter option: ')
                if user_input == '1':
                    account_dic[pin]['Acc_type'][acc_type[select_acc]].show_balance()
                    break
                elif user_input == '2':
                    money = int(input('\nHow much money you want to withdraw: '))
                    account_dic[pin]['Acc_type'][acc_type[select_acc]].withdrawl(money)
                    break
                elif user_input == '3':
                    money = int(input('\nHow much money you want to deposit: '))
                    account_dic[pin]['Acc_type'][acc_type[select_acc]].deposit(money)
                    break
                elif user_input == '4':
                    print('\nThank you !')
                    break
                else:
                    print("Something's Wrong ! Please try again !")
                    break
            else:
                print("\nYou do not have this account in bank. Please try again !")
                continue
        elif select_acc == '4':
            print('\nThank you!')
            break
        else:
            print("Something's Wrong ! Please try again !")
            continue

# Account Creation >> GLobal Variables


vinay_checking_acc = CheckingAccount(1, 'Vinay', 10000)
vivek_saving_acc = SavingAccount(2, 'Vivek', 20000)
vivek_business_acc = BusinessAccount(2, 'Vivek', 30000)

account_dic = {'1': {'Owner': 'Vinay', 'Acc_type': {'Checking': vinay_checking_acc}},
               '2': {'Owner': 'Vivek', 'Acc_type': {'Saving': vivek_saving_acc, 'Business': vivek_business_acc}}}

# Wrapping FUnction


def main():
    while True:

        print('\nWelcome to 24 Hour ATM Service !!\nPlease Insert Your ATM card...')
        pin = input('\nPlease Enter PIN: ')

        if pin in account_dic.keys():
            print(f"\nWelcome {account_dic[pin]['Owner']} !")
            atm_operation(pin)
        else:
            print('\nWrong PIN ! Please try again !')
            continue


if __name__ == '__main__':
    main()
