ROW_COUNT, COL_COUNT = [int(el) for el in input().split()]

matrix = []
delivery_position = None
initial_delivery_position = []


def is_valid(given_row, given_col):
    return 0 <= given_row < ROW_COUNT and 0 <= given_col < COL_COUNT


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row_index in range(ROW_COUNT):
    row_data = list(input())
    if 'B' in row_data:
        col_index = row_data.index('B')
        initial_delivery_position = [row_index, col_index]
        delivery_position = [row_index, col_index]
    matrix.append(row_data)

while True:
    direction = input()
    boy_row, boy_col = delivery_position
    row_to_go, col_to_go = direction_mapper[direction]
    next_row = boy_row + row_to_go
    next_col = boy_col + col_to_go

    if not is_valid(next_row, next_col):
        matrix[initial_delivery_position[0]][initial_delivery_position[1]] = ' '
        print("The delivery is late. Order is canceled.")
        break

    if matrix[next_row][next_col] == '*':
        continue

    if matrix[next_row][next_col] == 'A':
        matrix[boy_row][boy_col] = '.'
        delivery_position = [next_row, next_col]
        matrix[next_row][next_col] = 'P'
        matrix[initial_delivery_position[0]][initial_delivery_position[1]] = 'B'
        print("Pizza is delivered on time! Next order...")
        break

    if matrix[next_row][next_col] == 'P':
        matrix[boy_row][boy_col] = '.'
        delivery_position = [next_row, next_col]
        matrix[next_row][next_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
        continue

    # if not matrix[boy_row][boy_col] == 'R':
    #     matrix[boy_row][boy_col] = '.'
    #
    # delivery_position = [next_row, next_col]
    # matrix[next_row][next_col] = '.'

    if matrix[next_row][next_col] == '-':
        if not matrix[boy_row][boy_col] == 'R':
            matrix[boy_row][boy_col] = '.'

    delivery_position = [next_row, next_col]
    matrix[next_row][next_col] = '.'

for row in matrix:
    print(*row, sep="")


# OR -------------------------------------------------------------------------------------------

def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row-1, rows):
        return current_row-1, current_col
    if command == 'down' and is_valid(current_row+1, rows):
        return current_row+1, current_col
    if command == 'left' and is_valid(current_col-1, cols):
        return current_row, current_col-1
    if command == 'right' and is_valid(current_col+1, cols):
        return current_row, current_col+1
    return None, None


rows, cols = [int(x) for x in input().split(' ')]
field = []
start_row, start_col = None, None
boy_row, boy_col = None, None
line = ' '

for r in range(rows):
    row = list(input())
    field.append(row)
    if 'B' in row:
        boy_row = r
        boy_col = row.index('B')
        start_row = boy_row
        start_col = boy_col

while line:
    line = input()
    next_row, next_col = next_move(line, boy_row, boy_col)
    if next_row is None or next_col is None:
        print('The delivery is late. Order is canceled.')
        field[start_row][start_col] = ' '
        break
    if field[next_row][next_col] == '*':
        continue
    if field[next_row][next_col] == 'A':
        field[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        field[boy_row][boy_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        field[start_row][start_col] = 'B'
        break
    if field[next_row][next_col] == 'P':
        field[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        field[next_row][next_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
        continue
    if not field[boy_row][boy_col] == 'R':
        field[boy_row][boy_col] = '.'
    boy_row, boy_col = next_row, next_col
    field[boy_row][boy_col] = '.'

for row in field:
    print(''.join(row))
    
# 5 6
# *----A
# *B***-
# *-***-
# *----P
# ******
# down
# down
# right
# right
# right
# right
# up
# up
# up

# 5 6
# *----A
# *B***-
# *-***-
# *----P
# ******
# down
# down
# left
# right
# right
# right
# right
# right
# up
