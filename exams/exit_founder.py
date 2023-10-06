first, second = input().split(', ')
matrix = []

for row in range(6):
    matrix.append(input().split())

first_needs_rest = False
second_needs_rest = False

while True:
    first_plr_coordinates = input()
    if not first_needs_rest:
        coordinates = [int(digit) for digit in first_plr_coordinates if digit.isdigit()]
        position = matrix[coordinates[0]][coordinates[1]]
        if position == 'E':
            print(f"{first} found the Exit and wins the game!")
            break
        if position == 'T':
            print(f"{first} is out of the game! The winner is {second}.")
            break
        if position == 'W':
            print(f"{first} hits a wall and needs to rest.")
            first_needs_rest = True
    else:
        first_needs_rest = False

    second_player_coordinates = input()
    if not second_needs_rest:
        coordinates = [int(digit) for digit in second_player_coordinates if digit.isdigit()]
        position = matrix[coordinates[0]][coordinates[1]]
        if position == 'E':
            print(f"{second} found the Exit and wins the game!")
            break
        if position == 'T':
            print(f"{second} is out of the game! The winner is {first}.")
            break
        if position == 'W':
            print(f"{second} hits a wall and needs to rest.")
            second_needs_rest = True
    else:
        second_needs_rest = False

# Tom, Jerry
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)
