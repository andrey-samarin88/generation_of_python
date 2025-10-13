s = input().split()
new_s = [s[-1]] + s[:-1]
print(*new_s)