def sum_nums(*args):
    return args


print(sum_nums(5))  # prints (5, ) - tuple
print(sum_nums())  # prints empty tuple ()
print(sum_nums(1, 2, 3, 4, 5, 6, 7, 8, 9))  # prints (1, 2, 3, 4, 5, 6, 7, 8, 9) - tuple


def sum_nums(a, b, *args):
    return args


print(sum_nums(5, 6, 7))  # prints (7,) because the function returns the args only
print(sum_nums(1, 2))  # prints empty tuple ()
print(sum_nums(1, 2, 3, 4, 5, 6, 7, 8, 9))  # prints (3, 4, 5, 6, 7, 8, 9) because 1 and 2 are packed outside


