n = int(input())
s = [int(input()) for _ in range(0, n)]
a = int(input())

res = "НЕТ"
for i in range(0, n):
    for j in range(0, n):
        if s[i] * s[j] == a and i != j:
            res = "ДА"
print(res)
