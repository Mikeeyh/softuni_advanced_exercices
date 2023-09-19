from collections import deque

chocolates_available = [int(x) for x in input().split(', ')]
milk_cups = deque(int(x) for x in input().split(', '))
milkshakes_prepared = 0

while chocolates_available and milk_cups and milkshakes_prepared < 5:

    if chocolates_available[-1] <= 0 and milk_cups[0] <= 0:
        chocolates_available.pop()
        milk_cups.popleft()
        continue
    if chocolates_available[-1] <= 0:
        chocolates_available.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue

    if chocolates_available[-1] == milk_cups[0]:
        chocolates_available.pop()
        milk_cups.popleft()
        milkshakes_prepared += 1
    else:
        milk_cups.rotate(-1)  # equals to move the element at the last position
        chocolates_available[-1] -= 5

if milkshakes_prepared == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(x) for x in chocolates_available]) if chocolates_available else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in milk_cups]) if milk_cups else 'empty'}")

# OR --------------------------------------------------------------------------------------------

chocolates = deque(map(int, input().split(', ')))
milk = deque(map(int, input().split(', ')))
milkshakes = 0

while milkshakes < 5 and chocolates and milk:
    # Get the last chocolate and the first cup of milk
    last_chocolate = chocolates.pop()
    first_milk = milk.popleft()

    # Check if any ingredient is less than or equal to 0
    if last_chocolate <= 0 and first_milk <= 0:
        continue
    elif first_milk <= 0 < last_chocolate:
        chocolates.append(last_chocolate)
        continue
    elif last_chocolate <= 0 < first_milk:
        milk.appendleft(first_milk)
        continue

    # Check if the ingredients match
    if last_chocolate == first_milk:
        milkshakes += 1
    else:
        # Decrease the value of chocolate by 5 without moving it
        last_chocolate -= 5
        chocolates.append(last_chocolate)
        # Put the cup of milk at the end of the sequence
        milk.append(first_milk)

# Output
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {'empty' if not chocolates else ', '.join(map(str, chocolates))}")
print(f"Milk: {'empty' if not milk else ', '.join(map(str, milk))}")
# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55
