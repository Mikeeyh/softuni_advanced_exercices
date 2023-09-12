# STACKS

stack = []

stack.append(5)
stack.append(10)
stack.append(2)

print(stack.pop())
# remove the last element |||| print(stack[0]) - we do not use index in stacks

while stack:
    print(stack.pop())
    print(stack)

# QUEUES

from collections import deque
queue = deque(['Eric', 'John', 'Mike'])
queue.append('Maraya')
queue.popleft()
print(queue)

# ROTATE with negative
children = deque(input().split())
children.rotate(-1)
print(children) # If we have "T", "E"", "D" we move "T" to the last position --> "E", "D", "T"

children = deque(input().split())
children.rotate(-2)
print(children) # If we have "T", "E"", "D" we move "T" to the last position --> "D", "T", "E"

# ROTATE with positive
children = deque(input().split())
children.rotate(1)
print(children) # If we have "T", "E"", "D" we move "D" to the first position --> "D", "T", "E"
