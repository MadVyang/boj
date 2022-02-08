import sys
from collections import deque

n, q = [int(x) for x in sys.stdin.readline().split()]
g = [{} for x in range(n+1)]
for i in range(n-1):
    a, b, c = [int(x) for x in sys.stdin.readline().split()]
    g[a][b] = c
    g[b][a] = c


for _ in range(q):
    k, v = [int(x) for x in sys.stdin.readline().split()]
    count = 0
    que = deque()
    que.append((v, 1234567898))
    vis = [False]*(n+1)
    while que:
        cur, usado = que.popleft()
        vis[cur] = True
        if usado >= k:
            count += 1
        for nxt in g[cur]:
            if vis[nxt]:
                continue
            que.append((nxt, min(g[cur][nxt], usado)))

    print(count-1)
