from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        symbol = symbols.popleft()
        collected_nectar = nectar.pop()
        bee = bees.popleft()
        if symbol == "+":
            total_honey += abs(bee + collected_nectar)
        elif symbol == "-":
            total_honey += abs(bee - collected_nectar)
        elif symbol == "*":
            total_honey += abs(bee * collected_nectar)
        else:
            if collected_nectar != 0:
                total_honey += abs(bee / collected_nectar)
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")

# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /
