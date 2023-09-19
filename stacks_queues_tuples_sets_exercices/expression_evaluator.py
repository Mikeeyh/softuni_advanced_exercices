from collections import deque

expression = input().split()
numbers = deque()

for char in expression:
    if char not in '+-*/':
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()

            if char == '+':
                numbers.appendleft(first_num + second_num)
            elif char == '-':
                numbers.appendleft(first_num - second_num)
            elif char == '*':
                numbers.appendleft(first_num * second_num)
            elif char == '/':
                numbers.appendleft(first_num // second_num)

print(numbers[0])

# OR Using EVAL ------------------------------------------------------------------------

from collections import deque

expression = input().split()
numbers = deque()

for char in expression:
    if char not in '+-*/':
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = str(numbers.popleft())
            second_num = str(numbers.popleft())

            if char != '/':
                numbers.appendleft(eval(first_num + char + second_num))
            else:
                numbers.appendleft(eval(first_num + '//' + second_num))

print(numbers[0])
