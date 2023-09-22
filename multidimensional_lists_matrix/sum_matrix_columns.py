data = input().split(", ")
rows = int(data[0])
columns = int(data[1])

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for col_index in range(columns):
    sums = 0
    for row_index in range(rows):
        sums += matrix[row_index][col_index]
    print(sums)

# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
