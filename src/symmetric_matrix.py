n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

res = 'YES'
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            res = 'NO'
            break
    if res == 'NO':
        break

print(res)

# Входные данные
# 3

# 1 2 3
# 2 1 2
# 3 2 1

# Подсказка
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
# (3,0) (3,1) (3,2) (3,3)
