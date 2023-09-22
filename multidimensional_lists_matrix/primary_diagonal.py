n = int(input())
matrix = []

for row_index in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

sum_diagonal = 0
for row_index in range(n):
    sum_diagonal += matrix[row_index][row_index]

print(sum_diagonal)  # returns the diagonal left to right

# AND --------------------------------------

n = int(input())
matrix = []

for row_index in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

index = 1
sum_diagonal = 0

for row_index in range(n):
    sum_diagonal += matrix[row_index][len(matrix[row_index]) - index]
    index += 1

print(sum_diagonal)  # returns the diagonal right to left

# 3
# 11 2 4
# 4 5 6
# 10 8 -12