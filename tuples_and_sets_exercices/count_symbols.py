my_tuple = sorted(tuple(char for char in input()))
char_passed = list()

for char in my_tuple:
    if char in char_passed:
        continue

    counter = my_tuple.count(char)
    char_passed.append(char)
    print(f"{char}: {counter} time/s")

# OR ----------------------------------------------------------------

text = tuple(input())

unique_symbols = sorted(set(text))

for char in unique_symbols:
    print(f"{char}: {text.count(char)} time/s")

# OR ----------------------------------------------------------------

text = sorted(tuple(input()))

my_dict = {}

for char in text:
    if char not in my_dict:
        my_dict[char] = 0
    my_dict[char] += 1

for key, value in my_dict.items():
    print(f"{key}: {value} time/s")
