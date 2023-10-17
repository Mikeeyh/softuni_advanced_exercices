n = int(input())
movements = input().split(', ')
matrix = []
hazelnut_count = 0
squirrel_position = None


def is_valid(given_row, given_col):
    return 0 <= given_row < n and 0 <= given_col < n


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row_index in range(n):
    row_data = list(input())
    if 's' in row_data:
        col_index = row_data.index('s')
        squirrel_position = [row_index, col_index]
    matrix.append(row_data)

for movement in movements:
    current_row, current_col = squirrel_position
    row_to_go, col_to_go = direction_mapper[movement]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    if not is_valid(desired_row, desired_col):
        print("The squirrel is out of the field.")
        break

    if matrix[desired_row][desired_col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        break

    elif matrix[desired_row][desired_col] == 'h':
        matrix[desired_row][desired_col] = 's'
        matrix[current_row][current_col] = '*'
        squirrel_position = [desired_row, desired_col]
        hazelnut_count += 1
        if hazelnut_count == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    elif matrix[desired_row][desired_col] == '*':
        matrix[desired_row][desired_col] = 's'
        matrix[current_row][current_col] = '*'
        squirrel_position = [desired_row, desired_col]

else:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnut_count}")

# OR --------------------------------------------------------------------


def make_a_move(row_, col_, matrix):
    found_hazelnuts = 0
    if not (0 <= row_ < len(matrix) and 0 <= col_ < len(matrix)):
        print("The squirrel is out of the field.")
        return
    if matrix[row_][col_] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        return
    if matrix[row_][col_] == 'h':
        found_hazelnuts += 1
    matrix[row_][col_] = '*'
    return found_hazelnuts, matrix


rows = int(input())
commands = input().split(", ")
field = []
hazelnuts = 0
die = False

for _ in range(rows):
    field.append(list(input()))

squirrel_position = []
for row in range(rows):
    for col in range(rows):
        if field[row][col] == 's':
            squirrel_position = [row, col]

field[squirrel_position[0]][squirrel_position[1]] = "*"

for command in commands:
    if command == 'left':
        squirrel_position[1] -= 1
    elif command == 'right':
        squirrel_position[1] += 1
    elif command == 'down':
        squirrel_position[0] += 1
    elif command == 'up':
        squirrel_position[0] -= 1
    result = make_a_move(squirrel_position[0], squirrel_position[1], field)
    if not result:
        die = True
        break
    count_hazelnuts, field = result[0], result[1]
    hazelnuts += count_hazelnuts
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if not die and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")

# 5
# left, left, up, right, up, up
# **h**
# t****
# *h***
# *h*s*
# *****