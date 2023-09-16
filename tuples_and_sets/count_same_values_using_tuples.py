numbers = tuple(float(number) for number in input().split())
print(type(numbers))

occurs = {}

for number in numbers:
    occurs[number] = numbers.count(number)

for key, value in occurs.items():
    print(f"{key} - {value} times")

# OR -----------------------------------------

numbers = tuple(float(number) for number in input().split())

occurs = {}

for number in numbers:
    if number not in occurs:
        occurs[number] = numbers.count(number)
        print(f"{number} - {numbers.count(number)} times")

# OR -----------------------------------------

numbers = tuple(map(float, input().split()))

occurs = {}

for number in numbers:
    if number not in occurs:
        occurs[number] = 0
    occurs[number] += 1

[print(f"{key} - {value} times") for key, value in occurs.items()]
