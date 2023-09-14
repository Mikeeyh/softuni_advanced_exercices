clothes = [map(int, input().split())]
rack_capacity = int(input())
rack_count = 0

while clothes:
    capacity_left = rack_capacity

    if capacity_left > clothes:
        capacity_left -= clothes
        clothes.pop()
    else:
        rack_count += 1
        rack_capacity = capacity_left

print(rack_count)
