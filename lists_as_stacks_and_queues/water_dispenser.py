from collections import deque

quantity_of_water = int(input())
water_line = deque()

name = input()
while name != "Start":
    water_line.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()

    if len(data) == 1:
        liters_to_give = int(data[0])
        person_name = water_line.popleft()
        if liters_to_give <= quantity_of_water:
            print(f"{person_name} got water")
            quantity_of_water -= liters_to_give
        else:
            print(f"{person_name} must wait")

    else:
        liters_to_fill = int(data[1])
        quantity_of_water += liters_to_fill

    command = input()

print(f"{quantity_of_water} liters left")