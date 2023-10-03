rows, cols = [int(x) for x in input().split(',')]
matrix = []
mouse = []
cheese = 0
possible_moves = {
                  'up': (-1, 0),
                  'down': (1, 0),
                  'left': (0, -1),
                  'right': (0, 1)
                  }

for row in range(rows):
    current_row = list(input())
    matrix.append(current_row)
    for col in range(cols):
        if matrix[row][col] == 'M':
            mouse = [row, col]
            matrix[row][col] = '*'
        if matrix[row][col] == 'C':
            cheese += 1


while cheese != 0:
    command = input()
    if command == 'danger':
        if cheese:
            print("Mouse will come back later!")
        break

    move = possible_moves[command]
    new_row = mouse[0] + move[0]
    new_col = mouse[1] + move[1]
    mouse = [new_row, new_col]

    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
        print('No more cheese for tonight!')
        break



[print(''.join(row)) for row in matrix]

# 5,5
# **M**
# T@@**
# CC@**
# **@@*
# **CC*
# left
# down
# left

# 4,8
# CC@**C*M
# T*@**CT*
# **@@@@**
# T***C***
# down
# right
# left
# down
# left
# danger
