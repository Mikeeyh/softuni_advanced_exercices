data = input().split(", ")
rows = int(data[0])
columns = int(data[1])

matrix = []
sub_matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

max_sum = float('-inf')
max_sum_sub_matrix = []

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]
        sum_elements = current_element + next_element + element_below + element_diagonal
        if max_sum < sum_elements:
            max_sum = sum_elements
            max_sum_sub_matrix = [
                [current_element, next_element],
                [element_below, element_diagonal]
            ]

print(*max_sum_sub_matrix[0])  # returns the elements without parentheses
print(*max_sum_sub_matrix[1])
print(max_sum)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0