from collections import deque
import math
import sys


n, m = [int(x) for x in sys.stdin.readline().strip().split()]
arr = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i, j = [int(x) for x in sys.stdin.readline().strip().split()]
    arr[i][j] = True
    arr[j][i] = True

mn = math.inf
mni = -1
for i in range(1, n+1):
    dis = [math.inf]*(n+1)
    dis[i] = 0
    vis = [False]*(n+1)
    q = deque()
    for j in range(1, n+1):
        if arr[i][j]:
            q.append((j, 1))
    while q:
        j, d = q.popleft()
        vis[j] = True
        dis[j] = min(dis[j], d)
        for k in range(1, n+1):
            if not vis[k] and arr[j][k]:
                q.append((k, d+1))
        # print(i, j, d)

    if mn > sum(dis[1:]):
        mn = sum(dis[1:])
        mni = i
    # print(i, sum(dis[1:]), dis[1:])
print(mni,)
