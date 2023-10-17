from collections import deque

times = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

ducky_dict = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0,
}

while times and tasks:
    current_time = times.popleft()
    current_task = tasks.pop()
    current_result = current_time * current_task

    if current_result > 240:
        times.append(current_time)
        tasks.append(current_task - 2)
        continue

    if 0 <= current_result <= 60:
        ducky_dict['Darth Vader Ducky'] += 1
    elif 61 <= current_result <= 120:
        ducky_dict['Thor Ducky'] += 1
    elif 121 <= current_result <= 180:
        ducky_dict['Big Blue Rubber Ducky'] += 1
    elif 181 <= current_result <= 240:
        ducky_dict['Small Yellow Rubber Ducky'] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")

for duck_type, counter in ducky_dict.items():
    print(f"{duck_type}: {counter}")

# 10 15 12 18 22 6
# 12 16 5 6 9 1
