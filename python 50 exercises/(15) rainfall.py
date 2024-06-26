#15/50 python 50 exercises: rainfall

def get_rainfall():
    DICT = {} #empty dict

    while True:
        city = input("Enter a city: ").strip() #city name input

        if not city: #if user inputs empty string, break
            break

        rain = input("Enter amount of rain: ").strip() #rainfall amount input
        DICT[city] = DICT.get(city, 0) + int(rain) #creates new key-values for new cities inputted, but also adds values to already existing cities

    for key, value in DICT.items():
        print(f'{key}: {value}') #iterate thru the dict as tuples (thanks to items()), then print the corresponding keys and values in the dict

get_rainfall()