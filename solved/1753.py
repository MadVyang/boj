import heapq
import math
import sys

v, e = [int(x) for x in input().split()]
k = int(input())
k -= 1
g = []
for i in range(v):
    g.append({})
for i in range(e):
    u, vv, w = [int(x) for x in sys.stdin.readline().strip().split()]
    u -= 1
    vv -= 1
    if vv not in g[u]:
        g[u][vv] = math.inf
    g[u][vv] = min(w, g[u][vv])

vis = [math.inf]*v
vis[k] = 0
q = []
heapq.heappush(q, [0, k])
# for i in range(v):
#     heapq.heappush(q, (vis[i], i))
while q:
    c, i = heapq.heappop(q)
    # print(c, i)
    if c > vis[i]:
        continue
    for j in g[i]:
        if vis[j] > vis[i]+g[i][j]:
            vis[j] = vis[i]+g[i][j]
            q.append((vis[j], j))

for i in vis:
    if i == math.inf:
        print('INF')
    else:
        print(i)
