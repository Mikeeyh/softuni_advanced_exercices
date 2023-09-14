from collections import deque

quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    current_order = orders[0]
    if current_order <= quantity:
        orders.popleft()
        quantity -= current_order
    else:
        break

if orders:
    left_orders = " ".join(map(str, orders))
    print(f"Orders left: {left_orders}")
else:
    print("Orders complete")

# OR ------------------------------------------------------------------------------------

orders = deque()

quantity = int(input())
orders_taken = input().split()

for current_order in range(len(orders_taken)):
    orders.append(int(orders_taken[current_order]))

print(max(orders))
orders_list = list(map(int, orders))

for order in orders_list:
    if order <= quantity:
        orders.popleft()
        quantity -= order
    else:
        break

if orders:
    left_orders = " ".join(map(str, orders))
    print(f"Orders left: {left_orders}")
else:
    print("Orders complete")

# 499
# 57 45 62 70 33 90 88 76 100 50