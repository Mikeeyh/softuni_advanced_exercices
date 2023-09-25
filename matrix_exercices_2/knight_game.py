n = int(input())
matrix = []
knights = []  # we will keep track of the coordinates of all knights on the board

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == 'K':
            knights.append([row, col])  # adding the coordinates of the current Knight found

removed_knights = 0

possible_moves = [(1, 2), (2, 1),
                  (-1, 2), (-2, 1),
                  (1, -2), (2, -1),
                  (-1, -2), (-2, -1)]  # Possible coordinates of K moves, ex:(1, 2) means 1 row down and 2 columns right

while True:
    max_hits = 0
    max_knight = [0, 0]  # we will keep the coordinates of the current Knight with max hits

    for k_row, k_col in knights:
        hits = 0

        for move in possible_moves:  # we set the new current coordinates of our possible hit
            new_row = k_row + move[0]
            new_col = k_col + move[1]
            if 0 <= new_row < n and 0 <= new_col < n:  # we check if the new coordinates are in the matrix
                if matrix[new_row][new_col] == 'K':
                    hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]  # we will keep the coordinates of the current Knight with max hits

    if max_hits == 0:  # we end the loop if no hits possible
        break

    knights.remove(max_knight)  # we remove the max knight
    matrix[max_knight[0]][max_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)

# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0
