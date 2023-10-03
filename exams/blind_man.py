rows, cols = [int(x) for x in input().split()]
matrix = []
moves = 0
opponents_touched = 0
my_position = []

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == "B":
            my_position = [row, col]
            matrix[row][col] = '-'

directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)}

while True:
    command = input()
    if command == 'Finish':
        break
    if opponents_touched == 3:
        break

    move = directions[command]
    new_row = my_position[0] + move[0]
    new_col = my_position[1] + move[1]

    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or matrix[new_row][new_col] == 'O':
        continue

    moves += 1
    if matrix[new_row][new_col] == 'P':
        opponents_touched += 1

    my_position = [new_row, new_col]

print('Game over!')
print(f"Touched opponents: {opponents_touched} Moves made: {moves}")

# OR -----------------------------------------------------------------------------------------


def find_my_cooridnates(r, c, mtrx):
    for row in range(r):
        for col in range(c):
            if mtrx[row][col] == "B":
                return [row, col]


def check_my_next_position(my_row, my_col, current_matrix):
    if 0 <= my_row < len(current_matrix) and 0 <= my_col < len(current_matrix[0]):
        next_position = current_matrix[my_row][my_col]
        if next_position == "O":
            return False
        elif next_position == "-":
            return [my_row, my_col], current_matrix, 0
        elif next_position == "P":
            current_matrix[my_row][my_col] = "-"
            return [my_row, my_col], current_matrix, 1


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input().split())


my_coordinates = find_my_cooridnates(n, m, matrix)
matrix[my_coordinates[0]][my_coordinates[1]] = "-"
result = False
touched_opponents = 0
moves_made = 0

while True:
    if touched_opponents == 3:
        break

    command = input()
    if command == 'Finish':
        break

    if command == 'up':
        result = check_my_next_position(my_coordinates[0] - 1, my_coordinates[1], matrix)
    elif command == 'down':
        result = check_my_next_position(my_coordinates[0] + 1, my_coordinates[1], matrix)
    elif command == 'left':
        result = check_my_next_position(my_coordinates[0], my_coordinates[1] - 1, matrix)
    elif command == 'right':
        result = check_my_next_position(my_coordinates[0], my_coordinates[1] + 1, matrix)

    if result:
        my_coordinates, matrix, touches = result
        touched_opponents += touches
        moves_made += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")

# 5 8
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -
# up
# up
# left
# Finish

# 4 4
# O B O -
# - P O P
# - - P -
# - - - -
# left
# right
# down
# right
# down
# right
# up
# right
# up
# down
# Finish
