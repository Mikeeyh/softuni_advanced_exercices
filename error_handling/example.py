a = [int(el) for el in input().split()]
index = int(input())

try:
    print(a[index])
except IndexError:
    print('Invalid index')
# the program try to print the result and if the index is out of the range, it prints Invalid index

# ----------------------------------------------------------------------------------------------------------

while True:  # the program will not stop until the reception of an integer
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Not valid number. Try again!")

# using more excepts----------------------------------------------------------------------------------------------------

a = [int(el) for el in input().split()]

try:
    index = int(input())
    print(a[index])

except ValueError:
    print('Invalid index type, please enter integer')
except IndexError:
    print(f'Invalid index for list with length {len(a)}')

# using finally----------------------------------------------------------------------------------------------------

a = [int(el) for el in input().split()]

try:
    index = int(input())
    print(a[index])

except ValueError:
    print('Invalid index type, please enter integer')
except IndexError:
    print(f'Invalid index for list with length {len(a)}')
finally:
    print('from finally')  # the code in 'finally' will always being executed.

# using finally and else ----------------------------------------------------------------------------------------------

a = [int(el) for el in input().split()]

try:
    index = int(input())
    print(a[index])

except ValueError:
    print('Invalid index type, please enter integer')
except IndexError:
    print(f'Invalid index for list with length {len(a)}')
else:
    print('from else')  # the code in 'else' will be executed if no errors found in excepts
finally:
    print('from finally')  # the code in 'finally' will always be executed.

# catching the exception object ------------------------------------------------------------------------------------------

a = [int(el) for el in input().split()]

try:
    index = int(input())
    print(a[index])

except ValueError as ex:
    print('Invalid index type, please enter integer')
except IndexError:
    print(f'Invalid index for list with length {len(a)}')
else:
    print('from else')
finally:
    print('from finally')
