import sys

sys.setrecursionlimit(1000000)


n = int(input())
if n == 1:
    print(0)
    exit()
g = {}
for i in range(n-1):
    a, b, c = [int(x) for x in sys.stdin.readline().strip().split()]
    if a not in g:
        g[a] = {}
    g[a][b] = c
    if b not in g:
        g[b] = {}
    g[b][a] = c


vis = [False]*(n+1)


def farthest(x):
    md, mdi = 0, x
    for i in g[x]:
        if vis[i]:
            continue
        vis[i] = True
        d, di = farthest(i)
        d += g[x][i]
        if md < d:
            md, mdi = d, di
    return md, mdi


vis = [False]*(n+1)
vis[1] = True
d, di = farthest(1)
# print(d, di)
vis = [False]*(n+1)
vis[di] = True
d, di = farthest(di)
print(d)
