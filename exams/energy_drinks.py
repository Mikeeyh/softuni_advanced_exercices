from collections import deque

caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])
MAX_CAFFEINE = 300
initial_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    current_sum = current_energy_drink * current_caffeine

    if current_sum + initial_caffeine > MAX_CAFFEINE:
        energy_drinks.append(current_energy_drink)
        initial_caffeine -= 30
        if initial_caffeine < 0:
            initial_caffeine = 0
    else:
        initial_caffeine += current_sum

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print('At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")


