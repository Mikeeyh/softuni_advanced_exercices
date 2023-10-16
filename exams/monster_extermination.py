from collections import deque

armor_value = deque([int(x) for x in input().split(',')])
striking_impact_value = [int(x) for x in input().split(',')]

total_count_monsters = len(armor_value)
monsters = 0

while armor_value and striking_impact_value:
    current_armor_value = armor_value.popleft()
    current_striking_impact_value = striking_impact_value.pop()

    if current_striking_impact_value >= current_armor_value:
        monsters += 1
        current_striking_impact_value -= current_armor_value
        if current_striking_impact_value != 0:
            if striking_impact_value:
                striking_impact_value[0] += current_striking_impact_value
            else:
                striking_impact_value.append(current_striking_impact_value)
    else:
        current_armor_value -= current_striking_impact_value
        armor_value.append(current_armor_value)


if monsters < total_count_monsters:
    print("The soldier has been defeated.")
else:
    print("All monsters have been killed!")

print(f"Total monsters killed: {monsters}")

# 20,15,10
# 5,15,10,25