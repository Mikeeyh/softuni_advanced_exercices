import os

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "numbers.txt")
file = open(file_path, "r")

total = 0

for line in file:
    current_num = int(line)
    total += current_num

print(total)
