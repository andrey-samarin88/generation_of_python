xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])
matrix = [['.'] * 8 for _ in range(8)]
matrix[x][y] = 'N'

for i in range(8):
    for j in range(8):
        INX = (x - j) * (y - i)
        if abs(INX) == 2:
            matrix[j][i] = '*'

for row in matrix:
    print(*row)

# Входные данные
# b6