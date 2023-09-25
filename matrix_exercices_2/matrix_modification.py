rows = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(rows)]

while True:
    command = input().split()
    action = command[0]
    if action == 'END':
        break

    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if row < 0 or row >= rows or col < 0 or col >= rows:
        print("Invalid coordinates")
        continue

    if action == 'Add':
        matrix[row][col] += value
    elif action == 'Subtract':
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")

# OR ------------------------------------------------------------------------

rows = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(rows)]

command = input()

while command != 'END':
    data = command.split()
    action = data[0]
    row = int(data[1])
    col = int(data[2])
    value = int(data[3])

    if row < 0 or row >= rows or col < 0 or col >= rows:
        print("Invalid coordinates")
        continue

    if action == 'Add':
        matrix[row][col] += value
    elif action == 'Subtract':
        matrix[row][col] -= value

    command = input()

[print(*row) for row in matrix]

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
