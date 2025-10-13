n = int(input())
s = [tuple(map(int, input().split())) for _ in range(0, n)]

one = two = three = four = 0
for x, y in s:
    if x > 0 and y > 0:
        one += 1
    elif x < 0 and y > 0:
        two += 1
    elif x < 0 and y < 0:
        three += 1
    elif x > 0 and y < 0:
        four += 1

print(f'''Первая четверть: {one}
Вторая четверть: {two}
Третья четверть: {three}
Четвертая четверть: {four}''')
