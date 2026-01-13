n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)

# Входные данные
#3
#3

#1 2 3
#4 5 6
#7 8 9

#0 2
