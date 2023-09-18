my_tuple = sorted(tuple(char for char in input()))
char_passed = list()

for char in my_tuple:
    if char in char_passed:
        continue

    counter = my_tuple.count(char)
    char_passed.append(char)
    print(f"{char}: {counter} time/s")
