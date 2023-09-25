def is_valid(rows, cols, size):  # return True or False, if we are in the matrix or not
    return 0 <= rows < size and 0 <= cols < size


n = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(n)]
bombs = input().split()

sums = 0
alive_cells = 0

for bomb in bombs:
    curr_bomb = bomb.split(',')
    r = int(curr_bomb[0])
    c = int(curr_bomb[1])
    current_element = matrix[r][c]

    for row in range(n):
        for col in range(n):
            if row == r and col == c and current_element > 0:
                if is_valid(r - 1, c, n):
                    if matrix[row - 1][col] > 0:
                        matrix[row - 1][col] -= current_element
                if is_valid(r + 1, c, n):
                    if matrix[row + 1][col] > 0:
                        matrix[row + 1][col] -= current_element
                if is_valid(r, c + 1, n):
                    if matrix[row][col + 1] > 0:
                        matrix[row][col + 1] -= current_element
                if is_valid(r, c - 1, n):
                    if matrix[row][col - 1] > 0:
                        matrix[row][col - 1] -= current_element
                if is_valid(r - 1, c - 1, n):
                    if matrix[row - 1][col - 1] > 0:
                        matrix[row - 1][col - 1] -= current_element
                if is_valid(r + 1, c + 1, n):
                    if matrix[row + 1][col + 1] > 0:
                        matrix[row + 1][col + 1] -= current_element
                if is_valid(r - 1, c + 1, n):
                    if matrix[row - 1][col + 1] > 0:
                        matrix[row - 1][col + 1] -= current_element
                if is_valid(r + 1, c - 1, n):
                    if matrix[row + 1][col - 1] > 0:
                        matrix[row + 1][col - 1] -= current_element

                matrix[row][col] = 0

for row in matrix:
    alive_cells += len([cell for cell in row if cell > 0])
    sums += sum([cell for cell in row if cell > 0])

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sums}")
[print(*row) for row in matrix]

# OR -------------------------------------------------------------------


def is_valid(rows, cols, size):  # return True or False, if we are in the matrix or not
    return 0 <= rows < size and 0 <= cols < size


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = input().split()

alive_cells = 0
sums = 0

for bomb in bombs:
    curr_bomb = bomb.split(',')
    r = int(curr_bomb[0])
    c = int(curr_bomb[1])
    current_element = matrix[r][c]

    if current_element > 0:  # Only process positive elements
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                row_to_check = r + row_offset
                col_to_check = c + col_offset

                if is_valid(row_to_check, col_to_check, n):
                    if matrix[row_to_check][col_to_check] > 0:
                        matrix[row_to_check][col_to_check] -= current_element

        matrix[r][c] = 0  # Set the current cell to 0

# Calculate alive cells and sum
for row in matrix:
    alive_cells += len([cell for cell in row if cell > 0])
    sums += sum([cell for cell in row if cell > 0])

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sums}")
[print(*row) for row in matrix]

# 4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0
