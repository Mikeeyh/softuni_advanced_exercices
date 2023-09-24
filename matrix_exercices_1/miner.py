def is_valid(row, col, size):  # return True or False, if we are in the matrix or not
    return 0 <= row < size and 0 <= col < size


field_size = int(input())
commands = input().split()

matrix = []
current_row, current_column = 0, 0
coal = 0
game_over = False

for r in range(field_size):
    matrix.append(input().split())
    for c in range(field_size):
        if matrix[r][c] == 's':
            current_row, current_column = r, c  # start position of the miner
        elif matrix[r][c] == 'c':
            coal += 1

for command in commands:
    if command == 'up':
        if is_valid(current_row - 1, current_column, field_size):  # row-1, if we are in the matrix for future position
            current_row -= 1  # because we go up so the row index decrease
    elif command == 'down':
        if is_valid(current_row + 1, current_column, field_size):
            current_row += 1
    elif command == 'left':
        if is_valid(current_row, current_column - 1, field_size):
            current_column -= 1
    elif command == 'right':
        if is_valid(current_row, current_column + 1, field_size):
            current_column += 1

    if matrix[current_row][current_column] == 'e':
        print(f"Game over! ({current_row}, {current_column})")
        game_over = True
        break
    elif matrix[current_row][current_column] == 'c':
        coal -= 1
        matrix[current_row][current_column] = '*'
        if coal == 0:
            print(f"You collected all coal! ({current_row}, {current_column})")
            game_over = True
            break

if not game_over:
    print(f"{coal} pieces of coal left. ({current_row}, {current_column})")

# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *