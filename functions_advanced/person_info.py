def get_info(name, age, town):
    return f'This is {name} from {town} and he is {age} years old'


print(get_info('Mike', '25', 'Sofia'))

# OR -----------------------------------------


def get_info(name, town, age):
    return f'This is {name} from {town} and he is {age} years old'


info = {'name': 'Mike', 'town': 'Sofia', 'age': 20}
info_2 = ['Mike', 'Sofia', 20]
print(get_info(**info))  # unpacking dictionary **
print(get_info(*info_2))  # unpacking  list or tuple *
