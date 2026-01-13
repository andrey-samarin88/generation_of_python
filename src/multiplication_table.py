n, m = 10, 10

matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = str((i + 1) * (j + 1)).ljust(3)
    print(*matrix[i])
