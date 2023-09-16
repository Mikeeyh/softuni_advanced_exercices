# TUPLE

# count
numbers = (1, 2, 1, 3, 1)
numbers.count(1)  # returns the number of times a specific value occurs / 3 times '1'

# index
names = ("Pesho", "Gosho", "Gosho")
names.index("Gosho")  # returns the index of a particular element // index = 1 in this case

# unpacking
nums = (1, 2, 3)
a, b, c = nums  # returns a = 1, b = 2, c = 3 /// if we use less or more variables to unpack it will return an error

# convert a list to a tuple with function 'tuple' + comprehension
numbers = tuple(int(number) for number in input().split())

# SET - unordered and every element of a set is unique

set1 = {1, 2, 3, 1}
print(set1)  # returns {1, 2, 3}

# union, intersection, subset, superset, difference, sym_diff
# to use the methods you should type < a.union(b) > for example
a = {1, 2, 3}
b = {3, 4, 5}

union = a | b
intersection = a & b
subset = a < b
superset = a > b
difference = a - b
sym_diff = a ^ b

print(union)  # {1, 2, 3, 4, 5}  /// returns the combination of the two sets
print(intersection)  # {3}       /// returns the same elements of the two sets
print(subset)  # False           /// because the set 'a' is not a subset of 'b'
print(superset)  # False         /// because the 'a' is not bigger than 'b' so b is not subset of a
print(difference)  # {1, 2}      /// returns all elements which are not the same in 'b'
print(sym_diff)  # {1, 2, 5}     /// returns all elements which are inique from the two sets 'a' and 'b'

# example of true subset
c = {1, 2, 3}
d = {1, 2}
print(d < c)  # True because {1, 2} is in {1, 2, 3}

# set comprehension
nums = [1, 2, 3, 4, 4, 5, 6, 2, 1]
unique_set = {num for num in nums}  # {1, 2, 3, 4, 5, 6}

