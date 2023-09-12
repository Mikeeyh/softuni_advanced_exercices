from collections import deque

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

# from collections import deque
queue = deque(['Eric', 'John', 'Mike'])
queue.append('Maraya')
queue.popleft()
print(queue)
