from datetime import datetime, timedelta

# Parse robot names and processing times
robots_info = input().split(";")
robots = {}

for robot_info in robots_info:
    name, processing_time = robot_info.split("-")
    robots[name] = int(processing_time)

# Parse the starting time
start_time_str = input()
start_time = datetime.strptime(start_time_str, "%H:%M:%S") + timedelta(seconds=1)

# Initialize the assembly line queue
assembly_line = []

# Process products until the "End" command
while True:
    product = input()
    if product == "End":
        break

    assembly_line.append(product)

# Process products with robots
robot_processing_time = {robot: 0 for robot in robots}

while assembly_line:
    current_product = assembly_line.pop(0)

    for robot_name, processing_time in robots.items():
        if robot_processing_time[robot_name] <= 0:
            print(f"{robot_name} - {current_product} [{start_time.strftime('%H:%M:%S')}]")
            robot_processing_time[robot_name] = processing_time
            break

    start_time += timedelta(seconds=1)

