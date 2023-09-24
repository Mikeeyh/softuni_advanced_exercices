from collections import deque

rows, columns = [int(x) for x in input().split()]
text = deque(input())

matrix = []

for row in range(rows):
    matrix.append(['' * columns])  # for ech row we append spaces multiplied by our columns
    for column in range(columns):
        if row % 2 == 0:
            matrix[row][column] = text[0]
        else:
            matrix[row][-1 - column] = text[0]  # -1 because we want to start from the last index
                                                # Adding -column to move from right to left
        text.rotate(-1)

[print(*row, sep='') for row in matrix]
