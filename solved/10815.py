import bisect

n = int(input())
ns = [int(x) for x in input().split()]
ns.sort()
m = int(input())
ms = [int(x) for x in input().split()]
a = []
for i in range(m):
    t = bisect.bisect(ns, ms[i])
    # print(t)
    if ns[t-1] == ms[i]:
        a.append('1')
    else:
        a.append('0')
print(' '.join(a))
