# TUPLE

# count
numbers = (1, 2, 1, 3, 1)
numbers.count(1) # returns the number of times a specific value occurs / 3 times '1'

# index
names = ("Pesho", "Gosho", "Gosho")
names.index("Gosho") # returns the index of a particular element // index = 1 in this case

# unpacking
nums = (1, 2, 3)
a, b, c = nums # returns a = 1, b = 2, c = 3 /// if we use less or more variables to unpack it will return an error

# convert a list to a tuple with function 'tuple' + comprehension
numbers = tuple(int(number) for number in input().split())
