n, m = list(map(int, input().split()))

set_n = set()
set_m = set()

for _ in range(n):
    number = int(input())
    set_n.add(number)

for _ in range(m):
    number = int(input())
    set_m.add(number)

intersection = set_n & set_m

for num in intersection:
    print(num)

# OR ------------------------------------------------------

n, m = (int(x) for x in input().split())

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())

for _ in range(m):
    m_set.add(input())

common_elements = n_set.intersection(m_set)

print('\n'.join(common_elements))