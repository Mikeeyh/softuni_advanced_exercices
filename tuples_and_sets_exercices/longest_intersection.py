n = int(input())
max_intersection = set()

for _ in range(n):
    current_pair_of_sets = input().split('-')
    first_start, first_end = list(map(int, current_pair_of_sets[0].split(',')))
    second_start, second_end = list(map(int, current_pair_of_sets[1].split(',')))

    first_set = set()
    second_set = set()
    for num in range(first_start, first_end + 1):
        first_set.add(num)

    for num in range(second_start, second_end + 1):
        second_set.add(num)

    current_intersection = first_set & second_set

    if len(current_intersection) > len(max_intersection):
        max_intersection = current_intersection

print(f"Longest intersection is {[num for num in max_intersection]} with length {len(max_intersection)}")

# OR -------------------------------------------------------------------------------

n = int(input())
longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split('-')
    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    intersection = first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {[num for num in longest_intersection]} with length {len(longest_intersection)}")

# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10