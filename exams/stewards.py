from collections import deque

seats = input().split(', ')
first_sequence = deque([int(x) for x in input().split(', ')])
second_sequence = deque([int(x) for x in input().split(', ')])
total_rotations = 0
seat_matches = []

while True:
    if len(seat_matches) == 3 or total_rotations == 10:
        break

    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()
    sum_nums = first_num + second_num
    current_ascii_symbol = chr(sum_nums)
    possible_first_seat = str(first_num) + current_ascii_symbol
    possible_second_seat = str(second_num) + current_ascii_symbol
    total_rotations += 1

    if possible_first_seat in seat_matches or possible_second_seat in seat_matches:
        continue

    if possible_first_seat in seats:
        seat_matches.append(possible_first_seat)
    elif possible_second_seat in seats:
        seat_matches.append(possible_second_seat)
    else:
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {total_rotations}")

# 17K, 20B, 3C, 15D, 31Z, 28F
# 20, 35, 15, 3, 2, 10
# 1, 15, 64, 53, 45, 46
