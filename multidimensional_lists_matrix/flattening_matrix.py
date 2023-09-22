rows = int(input())
my_list = []

for row_index in range(rows):
    col = [int(el) for el in input().split(", ")]
    my_list += col

print(my_list)
