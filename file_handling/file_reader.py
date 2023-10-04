import os

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "numbers.txt")
file = open(file_path, "r")

total = 0

for line in file:
    current_num = int(line)
    total += current_num

file.close()
print(total)

# OR

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "numbers.txt")
file = open(file_path, "r")

total = 0

for line in file.readlines():
    print(line, end="")
    total += int(line)

file.close()
print()
print(total)

