n = int(input())

matrix = []
bunny = []  # coordinates of the bunny

for row in range(n):
    matrix.append(input().split())
    for col in range(n):


possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
max_eggs = float('-inf')
max_direction = ''
max_eggs_matrix = []

for direction, move in possible_moves.items():
    eggs = 0
    current_eggs_matrix = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == 'X':
            break

        eggs += int(matrix[row][col])
        current_eggs_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and current_eggs_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = current_eggs_matrix

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)

# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
