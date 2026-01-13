n, m = 4, 2
s = ['и', 'швец', 'и', 'жнец', 'и', 'на', 'дуде', 'игрец']

# Создание и заполнение матрицы из списка "s"
# matrix = []
# i = 0
# for row in range(n):
#     chank = []
#     for column in range(m):
#         chank.append(s[i])
#         i += 1
#     matrix.append(chank)
# print(*matrix, sep='\n')

# Предварительное создание матрицы заполненной "0" с заданным количеством строк и столбцов
matrix_1 = [[0] * m for _ in range(n)]
matrix_2 = [[0] * n for _ in range(m)]

# Если дан список с данными (s)
i = 0
for row in range(n):
    for column in range(m):
        matrix_1[row][column] = s[i]
        matrix_2[column][row] = s[i]
        i += 1

for row in matrix_1:
    print(*row)
print()
for row in matrix_2:
    print(*row)

# Для ввода данных из консоли
# n, m = int(input()), int(input())
# for row in range(n):
#     for column in range(m):
#         elem = input()
#         matrix_1[row][column] = elem
#         matrix_2[column][row] = elem
#
# print(*matrix_1, sep='\n')
# print()
# print(*matrix_2, sep='\n')