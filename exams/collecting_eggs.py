from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
paper = deque([int(x) for x in input().split(', ')])
box_size = 50
filled_boxes = 0

while eggs and paper:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    current_paper = paper.pop()

    if current_egg == 13:
        first_paper = paper.popleft()
        paper.appendleft(current_paper)
        paper.append(first_paper)

    elif current_egg + current_paper <= box_size:
        filled_boxes += 1

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if paper:
    print(f"Pieces of paper left: {', '.join(map(str, paper))}")
# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9
