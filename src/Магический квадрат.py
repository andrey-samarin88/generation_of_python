n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

res = 'YES'
s = []
sample = sum(matrix[0])

if sum(matrix[j][j] for j in range(n)) != sample:  # Сумма чисел в гл. диаганали
    res = 'NO'
if sum(matrix[j][n - j - 1] for j in range(n)) != sample:  # Сумма чисел в п. диаганали
    res = 'NO'
for i in range(n):
    if sum(matrix[i]) != sample:  # Сумма чисел в строках
        res = 'NO'
        break
    if sum(matrix[j][i] for j in range(n)) != sample:  # Сумма чисел в столбцах
        res = 'NO'
        break
    for j in range(n):
        s.append(matrix[i][j])
        if not (1 <= matrix[i][j] <= n * n):
            res = 'NO'
            break
    if res == 'NO':
        break

if len(set(s)) < n * n:
    res = 'NO'

print(res)

# Подсказка
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
# (3,0) (3,1) (3,2) (3,3)

# Если вы заглянули в комментарии, чтобы разобраться, что требуется в этой задаче,
# вот краткое описание условий: Условия задачи: 1) Все числа в матрице должны находиться
# в диапазоне 1 ≤ x ≤ n²; 2) Все числа в матрице должны быть уникальными (без повторов);
# 3) sum([любая строка]) = sum([ любой столбец]) = sum([гл.диагональ]) = sum ([п.диагональ])