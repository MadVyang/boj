import sys


t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    d={}
    for i in range(n):
        a,b=sys.stdin.readline().strip().split()
        if not b in d:
            d[b]=[]
        d[b].append(a)
    s = 1
    for k in d:
        s *= len(d[k])+1
    print(s-1)
