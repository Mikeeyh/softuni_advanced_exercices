import os

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "read_me.txt")

file = open(file_path, "r")

print(file.read())  # prints the text from the file named - read_me.txt

# Start reading exact number of bytes ---------------------------------------------------------------------

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "read_me.txt")

file = open(file_path, "r")

print(file.read(2))  # it will read the first two chars in our file
print(file.read(2))  # it will read the next two chars in our file

# Read a line from the file -------------------------------------------------------------------------------

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "read_me.txt")

file = open(file_path, "r")

print(file.readline())  # it will print the first line
print(file.readline())  # it will print the next line

# Read lines from the file -------------------------------------------------------------------------------

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "read_me.txt")

file = open(file_path, "r")

for line in file.readlines():
    print(line)  # it will print the current line until no lines left

# for line in file:
#     print(line, end="")
