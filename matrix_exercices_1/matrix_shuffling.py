def are_coordinates_valid(r1, c1, r2, c2, r, c):
    return 0 <= r1 < r and 0 <= r2 < r and 0 <= c1 < c and 0 <= c2 < c


rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    line = input()
    if line == 'END':
        break

    command = line.split()
    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]

    if are_coordinates_valid(row1, col1, row2, col2, rows, columns):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print('Invalid input!')


# [print(*row) for row in matrix] == for row in matrix: print(row)

# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END