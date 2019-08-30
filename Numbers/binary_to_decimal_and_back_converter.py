# Program to convert binary number to decimal and vice versa

def bin_to_dec_conv(num):    # Function to convert binary number to decimal
    
    decimal = int('0b'+str(num),2)
    
    return decimal

def dec_to_bin_conv(num):    # Function to convert decimal number to binary
    
    binary = bin(num)
    
    return binary


while True:    # Wrapping function
    
    user_input = input('Would you like to convert A) binary to decimal B) decimal to binary? choose A/B or \
                       enter quit to exit: ')
    
    if user_input.lower() == 'a':
        
        bin_num = int(input('\nEnter the binary number to convert: '))
        
        dec_num = bin_to_dec_conv(bin_num)
        
        print(f'\n{bin_num} in decimal: {dec_num}')
        
        continue
        
    elif user_input.lower() == 'b':
        
        dec_num = int(input('\nEnter the decimal number to convert: '))
        
        bin_num = dec_to_bin_conv(dec_num)
        
        print(f'\n{dec_num} in binary: {bin_num[2:]}')
        
        continue
        
        
    elif user_input == 'quit':
        break
        
    else:
        print('Wrong input !')
        continue
