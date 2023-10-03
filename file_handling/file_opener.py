try:
    file = open("text.txt", "r")
    print("Found")
except FileNotFoundError:
    print("File not found")

"""
If we try to search for a file text.txt and it does not exist, the program will return <File not found>

If we add the file in our directory, it will return <Found>

If we add the file in other directory, named for example: my_dir, it will return <File not found>, 
until we change the path to file = open("my_dir/text.txt", "r")
"""

try:
    file = open("my_dir/text.txt", "r")
    print("Found")
except FileNotFoundError:
    print("File not found")

# Using Import OS -----------------------------------------------------------
import os

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "my_dir", "text.txt")

try:
    file = open(file_path, "r")
    print("Found")
except FileNotFoundError:
    print("File not found")
