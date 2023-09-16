names = int(input())
unique_names = set()

for _ in range(names):
    name = input()
    unique_names.add(name)

for name in unique_names:
    print(name)
