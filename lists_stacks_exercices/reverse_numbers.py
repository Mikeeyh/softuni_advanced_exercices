numbers = [x for x in input().split()]
stack = []

while numbers:
    stack.append(numbers.pop())

print(' '.join(stack))

# OR ---------------------------------------------------------------------------------------

numbers = list(input().split())
stack = []

for _ in range(len(numbers)):
    stack.append(numbers.pop())

print(" ".join(stack))
