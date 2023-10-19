exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time_in_minutes = arrival_hour * 60 + arrival_minutes

time_difference_in_minutes = exam_time - arrival_time_in_minutes

if time_difference_in_minutes < 0:
    print(f"Late")
elif 0 <= time_difference_in_minutes <= 30:
    print(f"On time")
elif time_difference_in_minutes > 30:
    print(f'Early')

hour = 0
minutes = abs(time_difference_in_minutes)
result = ''

if minutes >= 60:
    hour = minutes // 60
    minutes = minutes % 60

if hour > 0:
    result += f"{hour}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes:} minutes"

if time_difference_in_minutes > 0:
    result += " before the start"
elif time_difference_in_minutes < 0:
    result += " after the start"

print(result)

# OR

exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time_in_minutes = arrival_hour * 60 + arrival_minutes
time_difference_in_minutes = exam_time - arrival_time_in_minutes

status = "Late" if time_difference_in_minutes < 0 else "On time" if 0 <= time_difference_in_minutes <= 30 else "Early"

hour, minutes = divmod(abs(time_difference_in_minutes), 60)
result = f"{hour}:{minutes:02d} hours" if hour > 0 else f"{minutes} minutes"
result += " before the start" if time_difference_in_minutes > 0 else " after the start"

print(status)
print(result)

