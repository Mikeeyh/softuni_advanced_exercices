from collections import deque

armor_value = deque([int(x) for x in input().split(',')])
striking_impact_value = [int(x) for x in input().split(',')]

monsters = 0

while armor_value and striking_impact_value:
    current_armor_value = armor_value.popleft()
    current_striking_impact_value = striking_impact_value.pop()

    if current_striking_impact_value >= current_armor_value:
        monsters += 1
        current_striking_impact_value -= current_armor_value
        if striking_impact_value:
            striking_impact_value[-1] += current_striking_impact_value
        elif not striking_impact_value and current_striking_impact_value > 0:
            striking_impact_value.append(current_striking_impact_value)
    else:
        current_armor_value -= current_striking_impact_value
        armor_value.append(current_armor_value)

if not armor_value:
    print("All monsters have been killed!")
if not striking_impact_value:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters}")

# 20,15,10
# 5,15,10,25
