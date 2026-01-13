# Выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.
n = int(input())  # 3
matrix = [list(map(int, input().split())) for _ in range(n)]  # 1 2 3
                                                              # 4 5 6
                                                              # 7 8 9

for chank in matrix:
    count = 0
    average = sum(chank) / len(chank)
    for  elem in chank:
        if elem > average:
            count += 1
    print(count)
