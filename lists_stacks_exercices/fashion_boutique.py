clothes = list(map(int, input().split()))
rack_capacity = int(input())

rack_count = 0
current_rack = 0

for cloth in reversed(clothes):
    if current_rack + cloth <= rack_capacity:
        current_rack += cloth
    else:
        rack_count += 1
        current_rack = cloth

rack_count += 1  # Add one for the last rack

print(rack_count)
