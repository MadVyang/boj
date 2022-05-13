from collections import deque
import math
import sys


n, e = [int(x) for x in sys.stdin.readline().strip().split()]
arr = []
for i in range(n):
    arr.append({})
for i in range(e):
    a, b, c = [int(x) for x in sys.stdin.readline().strip().split()]
    arr[a-1][b-1] = c
    arr[b-1][a-1] = c
v1, v2 = [int(x) for x in sys.stdin.readline().strip().split()]
v1 -= 1
v2 -= 1


def solve(s, t):
    q = deque([(s, 0)])
    vis = [math.inf]*n
    vis[0] = 0
    mn = math.inf
    while q:
        v, d = q.popleft()
        if vis[v] < d:
            continue
        if v == t:
            mn = min(mn, d)
            continue
        for i in arr[v]:
            if vis[i] > d+arr[v][i]:
                vis[i] = d+arr[v][i]
                nxt = (i, vis[i])
                q.append(nxt)
    return mn


ans = min(solve(0, v1)+solve(v1, v2)+solve(v2, n-1),
          solve(0, v2)+solve(v2, v1)+solve(v1, n-1))
if ans == math.inf:
    ans = -1
print(ans)
