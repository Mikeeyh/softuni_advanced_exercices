# def even_odd(command, *args):
#     if command == "even":
#         result = [x for x in args if x % 2 == 0]
#         return result
#     else:
#         result = [x for x in args if x % 2 != 0]
#         return result
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))

# OR ------------------------------------------------------------------


def even_odd(*numbers, command):
    if command == "even":
        return [num for num in numbers if num % 2 == 0]
    elif command == "odd":
        return [num for num in numbers if num % 2 != 0]


result_even = even_odd(1, 2, 3, 4, 5, command="even")
result_odd = even_odd(1, 2, 3, 4, 5, command="odd")

print(result_even)  # This will print [2, 4]
print(result_odd)   # This will print [1, 3, 5]
