matrix = []
for _ in range(6):
    row_data = input().split()
    matrix.append(row_data)

position = list(map(int, input().strip("(").strip(")").split(", ")))
position_row, position_col = position

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break

    action = command[0]
    direction = command[1]
    row_to_go, col_to_go = direction_mapper[direction]
    next_row = position_row + row_to_go
    next_col = position_col + col_to_go

    if action == 'Create':
        value = command[2]
        if matrix[next_row][next_col] == '.':
            matrix[next_row][next_col] = value
        position_row, position_col = next_row, next_col

    elif action == 'Update':
        value = command[2]
        if matrix[next_row][next_col] != '.':
            matrix[next_row][next_col] = value
        position_row, position_col = next_row, next_col

    elif action == 'Delete':
        if matrix[next_row][next_col] != '.':
            matrix[next_row][next_col] = '.'
        position_row, position_col = next_row, next_col

    elif action == 'Read':
        if matrix[next_row][next_col] != '.':
            print(matrix[next_row][next_col])
        position_row, position_col = next_row, next_col

for row in matrix:
    print(''.join(row))

# OR --------------------------


def move(direction_, position_):
    if direction_ == 'up':
        position_[0] -= 1
    elif direction_ == 'down':
        position_[0] += 1
    elif direction_ == 'left':
        position_[1] -= 1
    elif direction_ == 'right':
        position_[1] += 1
    return position_


matrix = []
for _ in range(6):
    matrix.append(input().split())

position = list(map(int, input().strip("(").strip(")").split(", ")))

while True:
    command = input()
    if command == 'Stop':
        break
    current_command = command.split(", ")
    position = move(current_command[1], position)
    if current_command[0] == 'Create':
        if matrix[position[0]][position[1]] == '.':
            matrix[position[0]][position[1]] = current_command[2]
    elif current_command[0] == 'Update':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = current_command[2]
    elif current_command[0] == 'Delete':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = '.'
    elif current_command[0] == 'Read':
        if matrix[position[0]][position[1]] != '.':
            print(matrix[position[0]][position[1]])

for row in matrix:
    print(' '.join(row))

# . . . . . .
# . 6 . . . .
# G . S . t S
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .
# (1, 1)
# Create, down, r
# Update, right, e
# Create, right, a
# Read, right
# Delete, right
# Stop

