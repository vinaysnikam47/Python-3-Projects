# Program to find out cost of width X height floor area

while True:
 
    try:
        width = float(input('What is width of floor? '))
        height = float(input('\nWhat is height of floor? '))
        cost = float(input('\nWhat is cost of tile? '))
        
        total_cost = width*height*cost

        print(f'\nTotal cost to cover {width} X {height} floor is ₹{total_cost}')
        user_input = input('\nWould you like to calculate cost again? Y/N ')
        if user_input.lower() == 'y':
            continue
        break
        
    except:
        print('Wrong input !')
        continue
