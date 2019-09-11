# Have the user enter two cities and unit
# Program will tell the aerial distance between this cities 


from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent='my_application', timeout=10)


# Function to calculate distance between cities
def distance_calc():
    while True:
        try:
            first_city = input("\nEnter first city name: ")
            second_city = input('Enter second city name: ')
            print('Kilometer >> K')
            print('Miles >> M')
            unit = input('Enter unit K/M: ')

            location_1 = geolocator.geocode(first_city)
            location_2 = geolocator.geocode(second_city)

            coor1 = (location_1.latitude, location_1.longitude)
            coor2 = (location_2.latitude, location_2.longitude)
        except:
            print("Something's Wrong ! Please try again.")
            continue

        else:

            if unit.upper() == 'K':

                print(f"Aerial distance between {first_city} and {second_city} is {geodesic(coor1,coor2)}.")
                break

            elif unit.upper() == 'M':

                print(f"\nAerial distance between {first_city} and {second_city} is {geodesic(coor1,coor2).miles} miles.")
                break

            else:
                print('Wrong input !')
                continue


if __name__ == '__main__':
    distance_calc()
