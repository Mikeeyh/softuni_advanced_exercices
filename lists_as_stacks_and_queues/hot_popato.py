from collections import deque

children = deque(input().split())
n = int(input()) - 1

while len(children) != 1:
    children.rotate(-n) # removes the first on the queue and adds it to the last position
    print(f"Removed {children.popleft()}")

print(f"Last is {children.popleft()}")

# OR ---------------------------------------------

children = deque(input().split())
n = int(input()) - 1

while len(children) != 1:
    count = 0
    while count != n:
        removed = children.popleft()
        children.append(removed)
    print(f"Removed {children.popleft()}")

print(f"Last is {children.popleft()}")