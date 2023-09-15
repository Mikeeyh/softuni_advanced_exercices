from collections import deque

duration_green_light = int(input())
duration_free_window = int(input())
cars = deque()
total_cars_passed = 0
crashed = False

command = input()

while command != 'END':
    if command == 'green':
        current_green_light = duration_green_light

        while cars and current_green_light > 0:
            car = cars.popleft()
            car_length = len(car)

            if current_green_light >= car_length:
                total_cars_passed += 1
                current_green_light -= car_length
            else:
                if current_green_light + duration_free_window >= car_length:
                    total_cars_passed += 1
                    break
                else:
                    crashed = True
                    print("A crash happened!")
                    print(f"{car} was hit at {car[current_green_light + duration_free_window]}.")
                    break
    else:
        cars.append(command)

    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")

