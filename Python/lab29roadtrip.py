'''
road trip
'''

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}


def get_cities(city_to_visit, hops, tabs=0):
    print("--"*tabs, f"Hops remaining: {hops}")
    print("--"*tabs, f"From {city_to_visit} you can visit:")
    for city in city_to_accessible_cities[city_to_visit]:
        print("--"*(tabs), "", city)
        if hops != 1:                                                # ends recursive loop
        # for city in city_to_accessible_cities[city_to_visit]:
            get_cities(city, hops - 1, tabs + 1)


start = input('Enter a city to visit (Boston, New York, Albany, Portland, or Philadelphia): ')
number_of_hops = int(input('Enter the number of hops you want to take: '))
get_cities(start, number_of_hops)
