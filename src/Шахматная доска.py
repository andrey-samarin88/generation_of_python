n, m = [int(i) for i in input().split()]

matrix = [['.'] * m for _ in range(n)]

num_elem = 1
for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = '*'
        num_elem += 1
    print(*matrix[i])