n = int(input())
d = {}
for i in input().split():
    if int(i) not in d:
        d[int(i)] = 0
    d[int(i)] += 1
k = int(input())
if k not in d:
    d[k] = 0
print(d[k])
