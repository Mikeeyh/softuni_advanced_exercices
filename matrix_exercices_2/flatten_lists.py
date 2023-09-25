string = input().split('|')
matrix = []

for i in range(len(string) - 1, -1, -1):  # from the length of the string with step -1 to 0. ('-1' because exclusive)
    row = [int(x) for x in string[i].split()]
    if row:
        matrix.append(row)

[print(*row, sep=" ", end=" ") for row in matrix]

# OR

# for row in matrix:
#     print(*row, sep=" ", end=" ")
