from collections import deque

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
