n = int(input())
arr = [int(x) for x in input().split()]
d = {}
for i in arr:
    d[i] = 1
dd = [x for x in d]
dd.sort()
print(' '.join([str(x) for x in dd]))
