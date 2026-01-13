s = [i.strip('.,!?:;-') for i in input().lower().split()]

result = {}

for key in set(s):
    result[key] = s.count(key)
min_val = []
for key, value in result.items():
    if value == min(result.values()):
        min_val.append(key)
print(min(min_val))
