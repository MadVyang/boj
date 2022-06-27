import heapq
import math
import sys


n = int(input())
m = int(input())
g = {}
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a not in g:
        g[a] = {}
    if b in g[a]:
        g[a][b]=min(g[a][b], c)
    else:
        g[a][b] = c
s, e = map(int, sys.stdin.readline().split())

q = [(0, s)]
dijk = [math.inf]*(n+1)
dijk[s] = 0
while q:
    d, i = heapq.heappop(q)
    if d > dijk[i] or i not in g:
        continue
    for j in g[i]:
        if dijk[j] > g[i][j]+d:
            dijk[j] = g[i][j]+d
            heapq.heappush(q, (dijk[j], j))

print(dijk[e])
