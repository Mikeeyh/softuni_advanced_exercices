n = int(input())
fishes_quantity = 0
flag = False


def is_in_area(given_row, given_col):
    return 0 <= given_row < n and 0 <= given_col < n


matrix = []
ship_position = None

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row_index in range(n):
    row_data = list(input())
    if 'S' in row_data:
        col_index = row_data.index('S')
        ship_position = [row_index, col_index]
    matrix.append(row_data)

direction = input()

while direction != 'collect the nets':
    current_row, current_col = ship_position
    row_to_go, col_to_go = direction_mapper[direction]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    if not is_in_area(desired_row, desired_col):
        if direction == 'up':
            desired_col = current_col + col_to_go
            desired_row = n - 1
        elif direction == 'down':
            desired_col = current_col + col_to_go
            desired_row = 0
        elif direction == 'right':
            desired_row = current_row + row_to_go
            desired_col = 0
        elif direction == 'left':
            desired_row = current_row + row_to_go
            desired_col = n - 1

    if matrix[desired_row][desired_col] == 'W':
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. Last coordinates of the ship: [{desired_row},{desired_col}]")
        flag = True
        matrix[desired_row][desired_col] = '-'
        fishes_quantity = 0
        ship_position = [desired_row, desired_col]
        break

    elif matrix[desired_row][desired_col].isdigit():
        ship_position = [desired_row, desired_col]
        fishes_quantity += int(matrix[desired_row][desired_col])
        matrix[desired_row][desired_col] = '-'

    else:
        matrix[current_row][current_col] = '-'
        ship_position = [desired_row, desired_col]

    direction = input()

if not flag:
    if fishes_quantity >= 20:
        print("Success! You managed to reach the quota!")
    elif 0 <= fishes_quantity < 20:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fishes_quantity} tons of fish more.")
    if fishes_quantity > 0:
        print(f"Amount of fish caught: {fishes_quantity} tons.")

    current_row, current_col = ship_position
    matrix[current_row][current_col] = 'S'
    for row in matrix:
        print(''.join(row))

# 4
# ---S
# ----
# 9-5-
# 34--
# down
# down
# right
# down
# collect the nets

# 5
# S---9
# 777-1
# W333-
# 11111
# -----
# down
# down
# right
# down
# collect the nets


print([x if x == "e" else -1 for x in 'sometext'])