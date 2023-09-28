matrix = []
my_position = []
targets = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            my_position = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
targets_down = []

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'shoot':
        r = my_position[0] + directions[command[1]][0]  # new row = my_position + our direction
        c = my_position[1] + directions[command[1]][1]

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                targets -= 1  # all targets decrease
                targets_down.append([r, c])  # we add the target's coordinates which has been hit
                break
            r += directions[command[1]][0]  # we increase the values because we moved to the other position
            c += directions[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

    elif command[0] == 'move':
        steps = int(command[2])
        direction = command[1]
        if direction == 'up':
            r = my_position[0] - steps
            c = my_position[1]
        elif direction == 'down':
            r = my_position[0] + steps
            c = my_position[1]
        elif direction == 'right':
            r = my_position[0]
            c = my_position[1] + steps
        elif direction == 'left':
            r = my_position[0]
            c = my_position[1] - steps

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == '.':
            matrix[r][c] = 'A'
            matrix[my_position[0]][my_position[1]] = '.'  # we change the last position to '.' because we moved
            my_position = [r, c]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(row) for row in targets_down]

# OR --------------------------------------------------------------------------------------

matrix = []
my_position = []
targets = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            my_position = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
targets_down = []

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'shoot':
        r = my_position[0] + directions[command[1]][0]  # new row = my_position + our direction
        c = my_position[1] + directions[command[1]][1]

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                targets -= 1  # all targets decrease
                targets_down.append([r, c])  # we add the target's coordinates which has been hit
                break
            r += directions[command[1]][0]  # we increase the values because we moved to the other position
            c += directions[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

    elif command[0] == 'move':
        r = my_position[0] + directions[command[1]][0] * int(command[2])
        c = my_position[1] + directions[command[1]][1] * int(command[2])

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == '.':
            matrix[r][c] = 'A'
            matrix[my_position[0]][my_position[1]] = '.'  # we change the last position to '.' because we moved
            my_position = [r, c]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(row) for row in targets_down]

# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1
