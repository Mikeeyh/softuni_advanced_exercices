n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]  # [n-i-1] or (-i-1) because n = 3 but we have i = 0, 1, 2

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
