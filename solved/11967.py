from collections import deque
import sys


n, m = [int(x) for x in sys.stdin.readline().strip().split()]
arr = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, a, b = [int(x) for x in sys.stdin.readline().strip().split()]
    arr[y-1][x-1].append((b-1, a-1))

vis = [[False]*n for _ in range(n)]
tmp = [[0]*n for _ in range(n)]
light = [[False]*n for _ in range(n)]
light[0][0] = True
q = deque([(0, 0)])
ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while q:
    y, x = q.popleft()
    if vis[y][x]:
        continue

    if not light[y][x]:
        if tmp[y][x] < 1000:
            q.append((y, x))
        tmp[y][x] += 1
        continue

    vis[y][x] = True
    for b, a in arr[y][x]:
        light[b][a] = True

    for dy, dx in ds:
        if y+dy >= 0 and y+dy < n and x+dx >= 0 and x+dx < n and not vis[y+dy][x+dx]:
            q.appendleft((y+dy, x+dx))

ans = 0
for i in range(n):
    for j in range(n):
        if light[i][j]:
            ans += 1
print(ans)
