from collections import deque
import sys


t = int(input())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().strip().split())
    ds = [0]+[int(x) for x in sys.stdin.readline().strip().split()]
    g = {}
    for i in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        if y not in g:
            g[y] = {}
        g[y][x] = True
    w = int(sys.stdin.readline().strip())

    q = deque([(w, 0)])
    vis = [0]*(n+1)
    ans = 0
    while q:
        cur, time = q.popleft()
        if time < vis[cur]:
            continue
        if cur not in g:
            ans = max(ans, time+ds[cur])
            continue
        for next in g[cur]:
            if vis[next] < time+ds[cur]:
                vis[next] = time+ds[cur]
                q.append((next, time+ds[cur]))
    print(ans)
