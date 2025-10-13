s = [int(n) for n in input().split()]

res = 0
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        res += 1

print(res)

#входные данные:
#1 1 3 2 2 1 1 1 1
#1 2 2 4 5 5 6
#1 3 2 3 1