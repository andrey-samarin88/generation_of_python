import numpy as np

matrix1 = np.array([[1, 0, 8], [4, 1, 8], [5, 6, 8]])
matrix2 = np.array([[1, 2], [3, 4], [2, 5]])

res = matrix1 @ matrix2

for row in res:
    print(*row)
