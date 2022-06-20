from collections import deque
import math


n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])

y, x = 0, 0
cur = 2
fs = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
}
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            y, x = i, j
            arr[i][j] = 0
        elif arr[i][j] > 0:
            fs[arr[i][j]].append((i, j))

efs = fs[1][:]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def path():
    global y, x, cur
    q = deque()
    vis = [[False]*n for i in range(n)]
    q.append((y, x, 0))
    vis[y][x] = True

    r = []
    while q:
        i, j, d = q.popleft()
        if (i != y or j != x) and 0 < arr[i][j] < cur:
            r.append((d, i, j))
            continue
        for dy, dx in dirs:
            if 0 <= i+dy < n and 0 <= j+dx < n:
                if vis[i+dy][j+dx]:
                    continue
                if arr[i+dy][j+dx] <= cur:
                    q.append((i+dy, j+dx, d+1))
                    vis[i+dy][j+dx] = True
    if not r:
        return -1, -1, -1
    r.sort()
    return r[0]


ans = 0
eat = 0
while True:
    d, y, x = path()
    if y == -1:
        break
    arr[y][x] = 0
    eat += 1
    if eat == cur:
        cur += 1
        eat = 0
    ans += d
    # print(y, x, d)

print(ans)
