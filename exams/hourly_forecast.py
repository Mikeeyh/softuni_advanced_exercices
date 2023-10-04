def forecast(*args):
    my_dict = {}
    for location, weather in args:
        if location not in my_dict:
            my_dict[location] = weather

    sorted_result = sorted(my_dict.items(), key=lambda x: (x[1], x[0]))

    sunny = ''
    cloudy = ''
    rainy = ''

    for key, value in sorted_result:
        if value == 'Sunny':
            sunny += f'{key} - {value}\n'
        elif value == 'Cloudy':
            cloudy += f'{key} - {value}\n'
        elif value == 'Rainy':
            rainy += f'{key} - {value}\n'

    return sunny + cloudy + rainy


print(forecast(("Sofia", "Sunny"), ("London", "Cloudy"), ("New York", "Sunny")))
