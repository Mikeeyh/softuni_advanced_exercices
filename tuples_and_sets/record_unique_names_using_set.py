names = int(input())
unique_names = set()

for _ in range(names):
    name = input()
    unique_names.add(name)

for name in unique_names:
    print(name)

# Using set comprehension

names = int(input())

unique_names = {input() for _ in range(names)}

for name in unique_names:
    print(name)
