rows, columns = [int(x) for x in input().split()]
start_letter = ord('a')

for row in range(rows):
    for column in range(columns):
        print(f"{chr(start_letter + row)}{chr(start_letter + row + column)}{chr(start_letter + row)}", end=" ")
    print()
