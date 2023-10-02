numbers_dictionary = {}

command = input()
while command != "Search":
    number_as_string = command
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    command = input()

command = input()

while command != "Remove":
    searched = command
    if searched in numbers_dictionary:
        print(numbers_dictionary[searched])
    else:
        print("Number does not exist in dictionary")
    command = input()

command = input()

while command != "End":
    searched = command
    if searched in numbers_dictionary:
        del numbers_dictionary[searched]
    else:
        print("Number does not exist in dictionary")
    command = input()

print(numbers_dictionary)

# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End

# one
# 1
# Search
# one
# Remove
# two
# End
