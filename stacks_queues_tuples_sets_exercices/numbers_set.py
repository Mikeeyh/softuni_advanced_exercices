first = set(input().split())
second = set(input().split())

n = int(input())

for _ in range(n):
    data = input().split()
    action = data[0]
    command = data[1]

    if action == 'Add':
        if command == 'First':
            elements = data[2:]
            first.update(elements)
        elif command == 'Second':
            elements = data[2:]
            second.update(elements)

    elif action == 'Remove':
        if command == 'First':
            elements = data[2:]
            first.difference_update(elements)
        elif command == 'Second':
            elements = data[2:]
            second.difference_update(elements)

    else:
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")

first = sorted(map(int, first))
second = sorted(map(int, second))

print(*[int(num) for num in first], sep=', ')
print(*[int(num) for num in second], sep=', ')
