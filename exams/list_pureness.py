from collections import deque


def best_list_pureness(numbers, k):
    best_pureness = 0
    best_rotation = 0

    numbers = deque(numbers)

    for rotation in range(k):
        current_pureness = sum(i * num for i, num in enumerate(numbers))
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = rotation

        numbers.rotate(1)  # Rotate the list one position to the right

    return f"Best pureness {best_pureness} after {best_rotation} rotations"


print(best_list_pureness([4, 3, 2, 6], 4))

# OR ----------------------------------------------------------------


def best_pureness(numbers, K):
    best_pur = 0
    best_rotation = 0

    for rotation in range(K):
        current_pureness = sum(i * num for i, num in enumerate(numbers))
        if current_pureness > best_pur:
            best_pur = current_pureness
            best_rotation = rotation

        numbers = [numbers[-1]] + numbers[:-1]  # Rotate the list one position to the right

    return f"Best pureness {best_pur} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_pureness(*test)
print(result)
