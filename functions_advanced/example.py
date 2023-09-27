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


def example_function(**kwargs):
    return kwargs


print(example_function(num=5, name='Peter', id=2))  # creates a dictionary
# {'num': 5, 'name': 'Peter', 'id': 2}


def example_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    return kwargs
# num 5
# name Peter
# id 2


def ex_function(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
    return kwargs


ex_function(a=5, num=5, name='Peter', id=2)
# 5
# ()
# {'num': 5, 'name': 'Peter', 'id': 2}


def print_nums(a, b, c):
    print(a, b, c)


nums = [1, 2, 3]
print_nums(*nums)  # unpacking: prints 1 2 3


def some_func(name, age):
    print(f"{name} is {age} years old")


person = {'age': 20, 'name': 'Peter'}
some_func(person['name'], person['age'])  # Peter is 20 years old
some_func(**person)  # Peter is 20 years old

# UNPACKING:


def get_info(name, town, age):
    return f'This is {name} from {town}, and he is {age} years old'


info = {'name': 'Mike', 'town': 'Sofia', 'age': 20}
info_2 = ['Mike', 'Sofia', 20]
print(get_info(**info))  # unpacking dictionary **
print(get_info(*info_2))  # unpacking  list or tuple *
# This is Mike from Sofia, and he is 20 years old
# This is Mike from Sofia, and he is 20 years old
