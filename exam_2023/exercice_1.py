from collections import deque

fuels = [(int(x)) for x in input().split()]
consumptions = deque([(int(x)) for x in input().split()])
quantities = [(int(x)) for x in input().split()]
reached_alt = 0
reached_list = []
index = 0

for _ in range(4):
    current_fuel = fuels.pop()
    current_consumption = consumptions.popleft()
    current_sum = current_fuel - current_consumption

    if current_sum >= quantities[index]:
        reached_alt += 1
        reached_list.append(f"Altitude {index + 1}")
        print(f"John has reached: Altitude {index + 1}")
    else:
        print(f"John did not reach: Altitude {index + 1}")
        break
    index += 1

if reached_alt == len(quantities):
    print("John has reached all the altitudes and managed to reach the top!")

if reached_alt == 0:
    print(f"John failed to reach the top.")
    print("John didn't reach any altitude.")
elif reached_alt < len(quantities):
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_list)}")

# 200 90 40 100
# 20 40 30 50
# 50 60 80 90

# 40 66 123 100
# 10 30 70 33
# 40 55 77 100

# 199 190 100 100
# 20 40 30 50
# 50 60 70 80

# 40 66 123 66
# 70 30 70 33
# 40 55 77 100