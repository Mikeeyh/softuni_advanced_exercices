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


# SORTED - returns always a list
a = [10, -2, 4, 3]
print(a)  # [10, -2, 4, 3]
print(sorted(a))  # [-2, 3, 4, 10]

# Using lambda to sort by key element:
my_dict = {'Peter': 21, 'George': 18, 'John': 45}
sorted_dict = sorted(my_dict.items(),
                     key=lambda x: x[0])  # if we sort by key we use '0'
print(sorted_dict)  # [('George', 18), ('Peter', 21), ('John', 45)]

my_dict = {'Peter': 21, 'George': 18, 'John': 45}
sorted_dict = sorted(my_dict.items(),
                     key=lambda kvp: kvp[1]) # if we sort by value we use '1'
for kvp in sorted_dict:
    print(kvp)
# ('George', 18)
# ('Peter', 21)
# ('John', 45)

my_dict = {'Peter': 21, 'George': 18, 'John': 45}
sorted_dict = sorted(my_dict.items(),
                     key=lambda kvp: kvp[1],
                     reverse=True)  # or using -kvp[1] for numbers
for kvp in sorted_dict:
    print(kvp)
# ('John', 45)
# ('Peter', 21)
# ('George', 18)

# Using reverse to sort dictionary by key in descending order
my_dict = {'Peter': 21, 'George': 18, 'John': 45}
reversed_dict = sorted(my_dict.items(),
                       key=lambda x: x[0],
                       reverse=True)
# [('Peter', 21), ('John', 45), ('George', 18)]
