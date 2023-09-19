first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0] + " " + line[1]
    numbers = [int(num) for num in line[2:]]

    if command == "Add First":
        first_set.update(numbers)
    elif command == "Add Second":
        second_set.update(numbers)
    elif command == "Remove First":
        first_set.difference_update(numbers)
    elif command == "Remove Second":
        second_set.difference_update(numbers)
    elif command == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")

# OR ---------------------------------------------------------------------------

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