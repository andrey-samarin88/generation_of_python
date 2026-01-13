s = 'a b c d e f r g b'.split()
n = 2

# s, n = input().split(), int(input())

res = [s[i:i + n] for i in range(0, len(s), n)]

print(res)