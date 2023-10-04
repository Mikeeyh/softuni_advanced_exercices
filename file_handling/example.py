# # some commands:
# """
# w - open for writing, truncating the file first / No such file -> it will create it
# r - open for reading only
# x - create a new file and open it for writing
# a - open for writing, appending to the end of the file if it exists
# t - text mode (default)
# b - binary mode (for a file which is not a text file, such as photos, etc)
# '+' - open a disk file for updating (reading and writing)
# """
#
# email = input()
# password = input()
#
# file = open("users.txt", "w")  # w -> write: delete the last input and add the new one, r -> read
# file.write(email)  # add the input to the file
#
# print(email)
#
# # 'a' ------------------------------------------------------------------
# email = input()
#
# file = open("users.txt", "a")  # a -> append mode, it does not delete the last input
# file.write(email + "\n")  # add the input to the file
#
# print(email)
#
# # close() ------------------------------------------------------------------
# email = input()
#
# file = open("users.txt", "a")
# file.write(email + "\n")
#
# file.close()  # it closes the file in order to free some working space
# print(email)
#
# # WRITELANES is used to write multiply strings ------------------------------------------------------------------
#
# file = open("users.txt", "a")
# lines = ['Write\n', 'in\n', 'file\n', 'on\n', 'new\n', 'lines\n']
# file.writelines(lines)
#
#
# # 'r' ------------------------------------------------------------------
# email = input()
#
# file = open("users.txt", "r")  # it is read only mode, we cannot add anything
# file.write("Hello")
#
# file.close()
# print(email)
#
# # OR open, then write to file from other directory ------------------------------------------------------------------
# email = input()
#
# file = open("mike.txt", "w")
# file.write("Hello")
#
# file.close()
# print(email)
# # when we are in write mode, and we want to open a file from other directory, then write, it will create a new file
# # but if we use read mode, it will return an error because there is no such file in our directory
#
#
# # OR open, then write to file from other directory, adding the path ---------------------------------------------------
# email = input()
#
# file = open("./my_dir/mike.txt", "r")  # the path starts from the current script directory (softuni_advanced_exercices)
#
# file.write("Hello")
#
# file.close()
# print(email)
# # if we run terminal, then type 'pwd' it will show the absolute path
# # we can replace it -> \Users\Mike\PycharmProjects\softuni_advanced_exercices
#
# # Import OS ---------------------------------------------------
# print(__file__)  # prints the abs path
#
# import os
#
# WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))  # gives us the path
#
# file_path = WORKING_DIRECTORY_PATH + "./my_dir/mike.txt"
#
# print(file_path) # _> C:\Users\Mike\PycharmProjects\softuni_advanced_exercices\file_handling./my_dir/mike.txt
# # this can work but there is a difference of Mac,Linux -> /path/my_path/ and Windows -> \path\my_path\
#
# file = open(file_path, "w")
# file.write("Mike")
# file.close()
#
# # Import OS ---------------------------------------------------
# print(__file__)
#
# import os
#
# WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))  # gives us the path
#
# file_path = os.path.join(WORKING_DIRECTORY_PATH, "my_dir", "mike.txt")
# # using os.path.join we can concatenate the path correctly ignoring the type of OS
#
# print(file_path)
#
# file = open(file_path, "w")
# file.write("Mike")
# file.close()
#
# # Closing file automatically using WITH -------------------------------------------------------------------
# import os
#
# WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(WORKING_DIRECTORY_PATH, "my_dir", "some.txt")
#
# file = open(file_path, "a")
# file.write("Mike")
# file.close()
#
# print(file.closed)
#
# with open(file_path, "w") as file:  # using this block of code closes the file automatically
#     file.write("Hello, Mike")
#
# print(file.closed)

# Try to open a file  -------------------------------------------------------------------
file_path = input("Please enter correct file path: ")  # adding .\numbers.txt it will open numbers.txt and print the txt

try:
    with open(file_path, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Invalid path was given!")

