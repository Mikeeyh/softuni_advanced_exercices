from collections import deque

food_quantity = int(input())
orders_queue = deque([int(x) for x in input().split()]) # or deque(int(x) for x in input().split())

print(max(orders_queue))

while orders_queue and orders_queue[0] <= food_quantity:
    food_quantity -= orders_queue[0]
    orders_queue.popleft()

if orders_queue:
    print(f"Orders left:", end="")
    while orders_queue:
        print(f" {orders_queue.popleft()}", end="")
else:
    print("Orders complete")

# OR using WHYLE cycle------------------------------------------------------------------------------------

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

# OR using FOR cycle------------------------------------------------------------------------------------

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