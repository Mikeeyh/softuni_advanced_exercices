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