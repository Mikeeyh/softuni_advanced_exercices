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


while cheese > 0:
    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break

    move = possible_moves[command]
    row = mouse[0] + move[0]
    col = mouse[1] + move[1]
    mouse = [row, col]

    if row < 0 or row >= rows or col < 0 or col >= cols:
        print("No more cheese for tonight!")
        row = mouse[0]
        col = mouse[1]
        mouse = [row, col]
        break

    else:
        if matrix[row][col] == 'C':
            matrix[row][col] = '*'
            cheese -= 1
            if cheese == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break

        elif matrix[row][col] == '@':
            row = mouse[0]
            col = mouse[1]
            continue

        elif matrix[row][col] == 'T':
            matrix[row][col] = 'M'
            print("Mouse is trapped!")
            break

    matrix[mouse[0]][mouse[1]] = '*'
matrix[mouse[0]][mouse[1]] = 'M'


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
