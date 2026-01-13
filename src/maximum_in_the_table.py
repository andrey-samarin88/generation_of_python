n, m = int(input()), int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

row = column = 0
for i in range(n):
    for j in range(0, m):
        if matrix[i][j] > matrix[row][column]:
            row, column = i, j

print(row, column)

# Входные данные
# 3
# 3

# 1 2 3
# 4 5 6
# 7 8 9