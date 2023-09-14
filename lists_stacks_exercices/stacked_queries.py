from collections import deque

n = int(input())
my_stack = []

for _ in range(n):
    query = input().split()

    if query[0] == "1":
        my_stack.append(int(query[1]))
    elif my_stack:
        if query[0] == "2":
            my_stack.pop()
        elif query[0] == "3":
            print(max(my_stack))
        elif query[0] == "4":
            print(min(my_stack))

while my_stack:
    print(my_stack.pop(), end="")
    if my_stack:
        print(', ', end="")


# OR using a queue-----------------------------------------------------------------------------------------

queue = deque()
number_of_lines = int(input())
final_stack = []

for i in range(number_of_lines):
    command = input().split()

    if len(command) == 1:
        action = command[0]
        if action == "2":
            if queue:
                queue.popleft()
        if action == "3":
            if queue:
                max_number = max(queue)
                print(max_number)
        if action == "4":
            if queue:
                min_number = min(queue)
                print(min_number)

    elif len(command) == 2:
        number_to_add = command[1]
        current_number = int(command[1])
        queue.append(current_number)

for i in range(len(queue)):
    final_stack = list(map(str, queue)) # or final_stack.append(str(queue.popleft()))
print(", ".join(final_stack[::-1]))

# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4



