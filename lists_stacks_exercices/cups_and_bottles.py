from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = [int(x) for x in input().split()]

wasted_water = 0

while cups_capacity and bottles_capacity:
    current_cup = cups_capacity.popleft()
    current_bottle = bottles_capacity.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        cups_capacity.appendleft(current_cup)

if not cups_capacity:
    remaining_bottles = sum(bottles_capacity)
    print(f"Bottles: {' '.join(map(str, bottles_capacity))}")
else:
    remaining_cups = " ".join(map(str, cups_capacity))
    print(f"Cups: {remaining_cups}")
print(f"Wasted litters of water: {wasted_water}")

# OR ------------------------------------------------------------------------------------------------


def fill_the_cups(cups, bottles):
    water_wasted = 0

    while cups and bottles:
        curr_cup = cups.pop(0)
        curr_bottle = bottles.pop()

        if curr_bottle >= curr_cup:
            water_wasted += curr_bottle - curr_cup
        else:
            curr_cup -= curr_bottle
            cups.insert(0, curr_cup)

    if not cups:
        bottles_remaining = sum(map(int, bottles))
        print(f"Bottles: {bottles_remaining}")
    else:
        cups_remaining = " ".join(map(str, cups))
        print(f"Cups: {cups_remaining}")

    print(f"Wasted litters of water: {water_wasted}")


# Example usage:
cups_capacity = [int(x) for x in input().split()]
bottles_capacity = [int(x) for x in input().split()]
fill_the_cups(cups_capacity, bottles_capacity)
