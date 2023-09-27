presents_count = int(input())
neighbourhood_size = int(input())
neighbourhood = []

santa_position = []
total_nice_kids = 0
nice_kids_with_presents = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(neighbourhood_size):
    neighbourhood.append(input().split())
    for col in range(neighbourhood_size):
        if neighbourhood[row][col] == 'S':
            santa_position = [row, col]
            neighbourhood[row][col] = '-'
        elif neighbourhood[row][col] == 'V':
            total_nice_kids += 1

while presents_count > 0:
    command = input()
    if command == "Christmas morning":
        break
    row = santa_position[0] + directions[command][0]
    col = santa_position[1] + directions[command][1]
    santa_position = [row, col]

    if 0 <= row < neighbourhood_size and 0 <= col < neighbourhood_size:
        if neighbourhood[row][col] == "V":
            nice_kids_with_presents += 1
            presents_count -= 1
        elif neighbourhood[row][col] == "C":
            for position in directions.values():
                if presents_count == 0:
                    break
                new_row = santa_position[0] + position[0]
                new_col = santa_position[1] + position[1]
                if 0 <= new_row < neighbourhood_size and 0 <= new_col < neighbourhood_size:
                    if neighbourhood[new_row][new_col] == "V":
                        nice_kids_with_presents += 1
                        neighbourhood[new_row][new_col] = '-'
                        presents_count -= 1
                    elif neighbourhood[new_row][new_col] == "X":
                        neighbourhood[new_row][new_col] = '-'
                        presents_count -= 1

    neighbourhood[santa_position[0]][santa_position[1]] = "-"
neighbourhood[santa_position[0]][santa_position[1]] = "S"

if presents_count == 0:
    print("Santa ran out of presents!")

for row in neighbourhood:
    print(" ".join(row))

if nice_kids_with_presents == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_with_presents} nice kid/s.")
# 5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning
