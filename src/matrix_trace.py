# Следом квадратной матрицы называется сумма элементов главной диагонали.
n = int(input())  # 3
matrix = [list(map(int, input().split())) for _ in range(n)]  # 1 2 3
                                                              # 4 5 6
                                                              # 7 8 9
# matrix_trace = 0
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             matrix_trace += matrix[i][j]

matrix_trace = sum([matrix[i][i] for i in range(n)])

print(matrix_trace)