import os

try:
    os.remove("make_file_and_delete_it.txt")
except FileNotFoundError:
    print("File already deleted")
