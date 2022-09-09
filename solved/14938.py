import heapq
import math


n, m, r = [int(x) for x in input().split()]
arr = [0]+[int(x) for x in input().split()]
g = {}
for i in range(r):
    a, b, l = [int(x) for x in input().split()]
    if a not in g:
        g[a] = {}
    if b not in g:
        g[b] = {}
    g[a][b] = l
    g[b][a] = l


def solve(index):
    q = [(0, index)]
    vis = [math.inf]*(n+1)
    vis[index] = 0
    s = set()
    while q:
        dis, i = heapq.heappop(q)
        s.add(i)
        if i not in g:
            continue
        for j in g[i]:
            if g[i][j]+dis <= m and g[i][j]+dis < vis[j]:
                heapq.heappush(q, (g[i][j]+dis, j))
                vis[j] = g[i][j]+dis

    ans = 0
    # print(s, arr)
    for i in s:
        ans += arr[i]
    return ans


ans = 0
for i in range(1,n+1):
    ans = max(ans, solve(i))
print(ans)
