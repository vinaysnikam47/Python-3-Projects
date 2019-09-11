# Have the user enter cost and tax rate 
# Program will tell tax cost nad total cost of product


# Function to calculate tax cost and total cost
def tax_calculator(cost, rate):
    tax_cost = (cost * rate) / 100
    total_cost = cost + tax_cost

    return tax_cost, total_cost


# Wrapping function
def main():
    while True:

        try:
            user_input = float(input('\nEnter cost of the product:'))
            cost = float(user_input)
            rate = float(input('Enter GST rate in percentage: '))

            tax_cost, total_cost = tax_calculator(cost, rate)

            print(f'\nTax Cost = ₹{tax_cost}')
            print(f"Total_cost = ₹{total_cost}")
            break

        except:
            print("Something's wrong ! Please try again.")
            continue


if __name__ == '__main__':
    main()
