clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())

racks = 0

while clothes_stack:
    racks += 1
    current_rack_capacity = rack_capacity
    while clothes_stack and clothes_stack[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_stack.pop()
        # we just check the element we will work with clothes_stack[-1]
print(racks)

# OR -------------------------------------------------------------------------------------------------

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
