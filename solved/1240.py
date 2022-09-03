from collections import deque
import sys


n, m = map(int, sys.stdin.readline().strip().split())
t = {}
for i in range(n-1):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a not in t:
        t[a] = {}
    if b not in t:
        t[b] = {}
    t[a][b] = c
    t[b][a] = c


def bfs(a, b):
    vis = {a: True}
    q = deque([(a, 0)])
    ans = -1
    while q:
        c, d = q.popleft()
        if c == b:
            ans = d
            break
        for j in t[c]:
            if j not in vis:
                q.append((j, d+t[c][j]))
                vis[j] = True
    return ans


for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    if b in t[a]:
        print(t[a][b])
        continue
    print(bfs(a, b))
