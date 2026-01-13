n, m = [int(i) for i in input().split()]
matrix1 = [list(map(int, input().split())) for _ in range(n)]
input()
matrix2 = [list(map(int, input().split())) for _ in range(n)]

res = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix1[i][j] + matrix2[i][j])
    res.append(row)

for row in res:
    print(*row)
