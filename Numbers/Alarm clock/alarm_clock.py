# Alarm clock which starts ringing after time input given by user gets complete
# It also rings at time provided by user (Only in 24 hours)


import time
import winsound


def play_alarm():  # Function which helps alarm clock to ring

    while True:

        user_input = input('\nChoose between following options h/m/s/c/t: ')

        # Ring after user input hours
        if user_input.lower() == 'h':
            hour = int(input('After how many hours you would like an alarm clock to ring: '))
            print(f"\nThank you ! Alarm clock will ring after {hour} hour/hours.")
            total_seconds = hour * 60 * 60
            time.sleep(total_seconds)
            winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
            break

        # Ring after user input minutes
        elif user_input.lower() == 'm':
            minute = int(input('After how many minutes you would like an alarm clock to ring: '))
            print(f"\nThank you ! Alarm clock will ring after {minute} minute/minutes.")
            total_seconds = minute * 60
            time.sleep(total_seconds)
            winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
            break

        # Ring after user input seconds
        elif user_input.lower() == 's':
            second = int(input('After how many seconds you would like an alarm clock to ring: '))
            print(f"\nThank you ! Alarm clock will ring after {second} second/seconds.")
            total_seconds = second
            time.sleep(total_seconds)
            winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
            break

        # Ring after user input combined hours,minutes and seconds
        elif user_input.lower() == 'c':
            hour = int(input('Enter hours: '))
            minute = int(input('Enter minutes: '))
            second = int(input('Enter seconds: '))
            print(f"\nThank you ! Alarm clock will ring after {hour} hours,{minute} minutes and {second} seconds.")
            total_seconds = (hour * 60 * 60) + (minute * 60) + second
            time.sleep(total_seconds)
            winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
            break

        # Ring at time set by user
        elif user_input == 't':
            while True:
                set_time = input('Enter time HH:MM : ')

                if len(set_time) != 5:
                    print('Wrong input !')
                    print("Please provide time in correct format.")
                    continue

                else:
                    hour = int(set_time[:2])
                    minute = int(set_time[3:])

                    if hour > 23 or minute > 59:
                        print('Wrong input!')
                        continue

                    else:
                        h = int(time.strftime("%H"))
                        m = int(time.strftime("%M"))

                        if hour > h:
                            total_seconds = ((hour * 60 * 60) + (minute * 60)) - ((h * 60 * 60) + (m * 60))

                        elif hour == h:
                            if minute > m:
                                total_seconds = (minute * 60) - (m * 60)
                            else:
                                total_seconds = (23 * 60 * 60) + ((60 - (m - minute)) * 60)

                        else:
                            total_seconds = (((h + 1 + hour) * 60 * 60) + (minute * 60)) - ((h * 60 * 60) + (m * 60))

                        print(f"Thank you ! Alarm clock will start ringing at {hour} hours and {minute} minutes.")
                        time.sleep(total_seconds)
                        winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
                break
            break

        else:
            print('Wrong input ! Please try again.')
            continue


def main():  # Wrapping function

    while True:
        print('\nWelcome to alarm clock !')
        print("h >> Hour \nm >> Minute \ns >> Second \nc >> Combination \nt >> Time(24 hour clock)")
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
