rows = int(input())
my_list = []

for row_index in range(rows):
    col = [int(el) for el in input().split(", ")]
    my_list += col

print(my_list)

# OR --------------------------------------------------------

rows = int(input())
matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

flattened = []

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        flattened.append(matrix[row_index][col_index])

print(flattened)
