# Class of Laptop
class Laptop:

    def __init__(self, name='Laptop', price=30000, quantity=10):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, stock):
        if stock < self.quantity:
            self.quantity -= stock
            print('\nHappy Shopping !!')
        else:
            print('\nSorry insufficient stock !')


# Class of Mobile Phone
class MobilePhone:

    def __init__(self, name='Mobile Phone', price=12000, quantity=30):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, stock):
        if stock < self.quantity:
            print('\nHappy Shopping !!')
            self.quantity -= stock
        else:
            print('\nSorry insufficient stock !')


# Class of Earphone
class Earphone:

    def __init__(self, name='Earphone', price=700, quantity=50):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, stock):
        if stock < self.quantity:
            print('\nHappy Shopping !!')
            self.quantity -= stock
        else:
            print('\nSorry insufficient stock !')


# class of Powerbank
class PowerBank:

    def __init__(self, name='Power Bank', price=500, quantity=20):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, stock):
        if stock < self.quantity:
            print('\nHappy Shopping !!')
            self.quantity -= stock
        else:
            print('\nSorry insufficient stock !')
            

# Bill printing function
def bill_print(lap, mob, ear, power, ltp, m, e, p):

    print('\nHere is your Bill....')
    print('\n{0:^63}'.format('!! TECHNOLOGY SHOP !!'))
    print(' _______________________________________________________________')
    print('|{0:^14}|{1:^16}|{2:^14}|{3:^16}|'.format('Category', 'Price/item (₹)', 'Quantity', 'Total Cost (₹)'))
    print('|______________|________________|______________|________________|')
    if lap > 0:
        print('|{0:^14}|{1:^16}|{2:^14}|{3:^16}|'.format(ltp.name, ltp.price, lap, ltp.price*lap))
        print('|              |                |              |                |')
    pass
    if mob > 0:
        print('|{0:^14}|{1:^16}|{2:^14}|{3:^16}|'.format(m.name, m.price, mob, m.price*mob))
        print('|              |                |              |                |')
    pass
    if ear > 0:
        print('|{0:^14}|{1:^16}|{2:^14}|{3:^16}|'.format(e.name, e.price, ear, e.price*ear))
        print('|              |                |              |                |')
    pass
    if power > 0:
        print('|{0:^14}|{1:^16}|{2:^14}|{3:^16}|'.format(p.name, p.price, power, p.price*power))

    print('|______________|________________|______________|________________|')
    print('|{0:^14}|{1:^16}|{2:^14}|{3:^16}|'.format('Total', '--', (lap+mob+ear+power),
                                                     (ltp.price*lap+m.price*mob+e.price*ear+p.price*power)))
    print('|______________|________________|______________|________________|')  


# Main function
def main():
    print('Welcome to Technology Shop !!')
    ltp = Laptop()
    m = MobilePhone()
    e = Earphone()
    p = PowerBank()

    lap = 0
    mob = 0
    ear = 0
    power = 0

    while True:

        print("\n1. Buy Item")
        print("2. View Items")
        print('3. Print Bill')
        print('4. Exit')

        user_input = int(input('\nEnter option here: '))

        if user_input == 1:
            print('\n1. Laptop')
            print('2. Mobile Phone')
            print('3. Earphone')
            print('4. Power Bank')
            buying_item = int(input('\nWhat would you like to buy? Enter option here: '))

            if buying_item == 1:
                quant = int(input('How many Laptops you want to buy: '))
                lap += quant
                ltp.buy(quant)

            if buying_item == 2:
                quant = int(input('How many Mobile phones you want to buy: '))
                mob += quant
                m.buy(quant)

            if buying_item == 3:
                quant = int(input('How many Earphones you want to buy: '))
                ear += quant
                e.buy(quant)

            if buying_item == 4:
                quant = int(input('How many Power banks you want to buy: '))
                power += quant
                p.buy(quant)

        elif user_input == 2:
            print(' ____________________________________________')
            print('|{0:^14}|{1:^14}|{2:^14}|'.format('Category', 'Price/item (₹)', 'Quantity'))
            print('|______________|______________|______________|')
            print('|{0:<14}|{1:^14}|{2:^14}|'.format(ltp.name, ltp.price, ltp.quantity))
            print('|              |              |              |')
            print('|{0:<14}|{1:^14}|{2:^14}|'.format(m.name, m.price, m.quantity))
            print('|              |              |              |')
            print('|{0:<14}|{1:^14}|{2:^14}|'.format(e.name, e.price, e.quantity))
            print('|              |              |              |')
            print('|{0:<14}|{1:^14}|{2:^14}|'.format(p.name, p.price, p.quantity))
            print('|______________|______________|______________|')

        elif user_input == 3:
            if lap == 0 and mob == 0 and ear == 0 and power == 0:
                print("\nYou haven't bought anything yet !")
                continue
            elif lap > 0 or mob > 0 or ear > 0 or power > 0:
                bill_print(lap, mob, ear, power, ltp, m, e, p)

        elif user_input == 4:
            print('\nThank you for visiting our shop !')
            break


if __name__ == '__main__':
    main()
