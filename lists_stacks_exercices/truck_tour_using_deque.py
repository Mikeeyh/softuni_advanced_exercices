from collections import deque

n = int(input())
pumps = deque()
stops = 0

# we need to check where is the start possible position to start driving the truck
start_position = 0 # because we start from the pump in index 0

for _ in range(n):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)]) # using [] to be sure we add every list of 2 elements in our deque

while stops < n: # we stop the cycle when all the pumps are checked (n)
    fuel = 0

    for i in range(n):
        fuel += pumps[i][0] # we take the current pump using the index 'i' and the current fuel of it
        destination = pumps[i][1] # same as above but we take the current distance of the pump

        if fuel < destination:
            pumps.rotate(-1) # if the fuel is not enough we rotate the pumps to the left then we use '-1'
            start_position += 1 # to move to the other and try to start from there if fuel is not enough
            stops = 0
            break

        fuel -= destination
        stops += 1

print(start_position)