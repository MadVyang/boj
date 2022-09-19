from collections import deque
import heapq


n, m = map(int, input().split())
g = {}
mc = 0
for i in range(m):
    a, b, c = map(int, input().split())
    if a not in g:
        g[a] = {}
    if b not in g[a]:
        g[a][b] = 0
    if b not in g:
        g[b] = {}

    g[a][b] = max(g[a][b], c)
    g[b][a] = g[a][b]
    mc = max(mc, c)

x, y = map(int, input().split())


def check(c):
    global x, y
    v = [False]*(n+1)
    v[x] = True
    q = deque([x])
    while q:
        i = q.popleft()
        if i == y:
            return True
        for j in g[i]:
            if not v[j] and g[i][j] >= c:
                q.append(j)
                v[j]=True
    return False


left, right = 0, mc+1

while left < right:
    mid = left + (right - left) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid
print(right-1)
