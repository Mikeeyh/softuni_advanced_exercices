from collections import deque

bullet_price = int(input())
gun_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

bullets_used = 0
total_bullets_used = 0
locks_destroyed = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print("Bang!")
        locks_destroyed += 1
    else:
        locks.appendleft(current_lock)
        print("Ping!")

    bullets_used += 1
    total_bullets_used += 1

    if bullets_used == gun_size and bullets:
        print("Reloading!")
        bullets_used = 0

money_earned = intelligence_value - (bullet_price * total_bullets_used)
locks_left = len(locks)

if locks_left:
    remaining_locks = sum(map(int, locks))
    print(f"Couldn't get through. Locks left: {locks_left}")
else:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")

# 50
# 2
# 11 10 5 11 10 20
# 15 13 16
# 1500