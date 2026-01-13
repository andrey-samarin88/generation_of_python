import numpy as np

matrix = np.array([[1, 0], [4, 1]])

res = np.linalg.matrix_power(matrix, 25)

for row in res:
    print(*row)
