# Have user asked for cost of item and amount paid for item
# Program returns change to be returned

def change_return(cost,amount):    # Function to calculate change
    
    change = [2000,500,200,100,50,20,10,5,2,1]
    
    amount_to_be_returned = amount - cost
    
    remaining = amount_to_be_returned
    return_list = []
    
    i = 0
    
    while remaining != 0:
        
        if remaining < change[i]:
            i += 1
            continue     
        else:
            remaining = remaining - change[i]
            return_list.append(change[i])
            continue
        break
            
    return return_list,amount_to_be_returned
    
    
def main():    # Wrapping function
    
    change = [2000,500,200,100,50,20,10,5,2,1]

    cost = int(input('Enter cost of the item to be purchased? '))
    amount = int(input('Enter amount paid for the item? '))

    returns = change_return(cost,amount)

    print(f'\nTotal amount to be returned: ₹{returns[1]}')

    for note in change[:6]:
        if note in returns[0]:
            print(f'\nNotes of ₹{note}: {returns[0].count(note)}')
            

    for coin in change[6:]:
        if coin in returns[0]:
            print(f'\nNotes/Coins of ₹{coin}: {returns[0].count(coin)}')
            
            
            
if __name__ == '__main__':
    main()
        
