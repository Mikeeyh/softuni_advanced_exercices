matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][2])  # returns 6
print(matrix)  # returns [[1, 2, 3], [4, 5, 6]]

# Change a value:
matrix[0][1] = 100
print(matrix[0][1])  # returns 100
print(matrix)  # returns [[1, 100, 3], [4, 5, 6]]

# Change each value by 1
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] += 1
print(matrix)

# Creating a matrix
matrix = []
rows_count = 2
cols_count = 3

for row in range(rows_count):
    matrix.append([1, 2, 3])

print(matrix[0])  # returns [1, 2, 3]
print(matrix[1])  # returns [1, 2, 3]

# Creating a matrix
matrix = []
rows_count = 2
cols_count = 3
number = 1

for row_index in range(rows_count):
    matrix.append([])
    for col in range(cols_count):
        matrix[row_index].append(number)
        number += 1

print(matrix)  # returns [[1, 2, 3], [4, 5, 6]]

# Using Loops to traverse matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in range(len(matrix)):  # we have 3 rows -> len = 3
    for column in range(len(matrix[row])):  # we have 3 columns because there are 3 elements in each row
        print(matrix[row][column], end=" ")
    print()

# 1 2 3
# 4 5 6
# 7 8 9

