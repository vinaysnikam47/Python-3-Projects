# Alarm clock which plays sound after time input given bu user


import time
import winsound

def play_alarm():    # Function which plays sound of alarm

    while True:

        user_input = input('\nChoose between following option h/m/s/c: ')
    
        if user_input.lower() == 'h':
            hour = int(input('After how many hours you would like to play an alarm: '))
            print(f"\nThank you ! Alarm will play after {hour} hour/hours.")
            total_seconds = hour*60*60
            time.sleep(total_seconds)
            winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
            break
    
        
        elif user_input.lower() == 'm':
            minute = int(input('After how many minutes you would like to play an alarm: '))
            print(f"\nThank you ! Alarm will play after {minute} minute/minutes.")
            total_seconds = minute*60
            time.sleep(total_seconds)
            winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
            break
        
        elif user_input.lower() == 's':
            second = int(input('After how many seconds you would like to play an alarm: '))
            print(f"\nThank you ! Alarm will play after {second} second/seconds.")
            total_seconds = second
            time.sleep(total_seconds)
            winsound.PlaySound("alarm.wav",winsound.SND_ASYNC)
            break

        
        elif user_input.lower() == 'c':
            hour = int(input('Enter hours: '))
            minute = int(input('Enter minutes: '))
            second = int(input('Enter seconds: '))
            print(f"\nThank you ! Alarm will play after {hour} hours,{minute} minutes and {second} seconds.")
            total_seconds = (hour*60*60)+(minute*60)+second
            time.sleep(total_seconds)
            winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
            break

        else:
            print('Wrong input ! Please try again.')
            continue

def main():    # Wrapping function
        
    while True:    
        print('Welcome to alarm clock !')
        print("h >> Hour \nm >> Minute \ns >> Second \nc >> Combination")
        play_alarm()
        stop = input("\nWould you like to stop(S) an alarm or set an another(A) alarm S/A: ")
        
        if stop.lower() == 's':
            winsound.PlaySound(None, winsound.SND_PURGE)
            break
        elif stop.lower() == 'a':
            winsound.PlaySound(None, winsound.SND_PURGE)
            continue
        else:
            print("wrong Input!")
            break

if __name__ == '__main__':
    main()


    
    
    
    

    
    