rows, cols = [int(x) for x in input().split()]
matrix_1 = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum_1 = float('-inf')
max_row = 0
max_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += matrix_1[r][c]
        if current_sum > max_sum_1:
            max_sum_1 = current_sum
            max_row = row
            max_col = col

max_sub_matrix = [matrix_1[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]

print(f"Sum = {max_sum_1}")
[print(*row) for row in max_sub_matrix]

# OR ----------------------------------------------------------------

rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
max_sum_sub_matrix = []

for row_index in range(rows - 2):
    for col_index in range(columns - 2):
        current_element = matrix[row_index][col_index]
        next_element_1 = matrix[row_index][col_index + 1]
        next_element_2 = matrix[row_index][col_index + 2]
        element_below_1 = matrix[row_index + 1][col_index]
        element_below_2 = matrix[row_index + 2][col_index]
        element_diagonal_1 = matrix[row_index + 1][col_index + 1]
        element_diagonal_2 = matrix[row_index + 2][col_index + 2]
        element_next_diagonal_1 = matrix[row_index + 1][col_index + 2]
        element_next_below_2 = matrix[row_index + 2][col_index + 1]

        sum_elements = current_element + \
                       next_element_1 + \
                       element_below_1 + \
                       element_diagonal_1 + \
                       next_element_2 + \
                       element_next_diagonal_1 + \
                       element_below_2 + \
                       element_diagonal_2 + \
                       element_next_below_2

        if max_sum < sum_elements:
            max_sum = sum_elements
            max_sum_sub_matrix = [
                [current_element, next_element_1, next_element_2],
                [element_below_1, element_diagonal_1, element_next_diagonal_1],
                [element_below_2, element_next_below_2, element_diagonal_2],
            ]

print(f"Sum = {max_sum}")
print(*max_sum_sub_matrix[0])  # returns the elements without parentheses
print(*max_sum_sub_matrix[1])
print(*max_sum_sub_matrix[2])

# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4