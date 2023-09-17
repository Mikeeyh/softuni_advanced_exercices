commands = int(input())
car_numbers = set()

for _ in range(commands):
    direction, car_number = input().split(", ")

    if direction == 'IN':
        car_numbers.add(car_number)
    elif direction == 'OUT':
        car_numbers.remove(car_number)

if not car_numbers:
    print('Parking Lot is Empty')
else:
    for current_number in car_numbers:
        print(current_number)

# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU

# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA