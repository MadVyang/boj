
from collections import deque
import sys


m, n, h = [int(x) for x in input().split()]
arr = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append([int(x) for x in sys.stdin.readline().strip().split()])
    arr.append(tmp)

dirs = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

r = 0
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.appendleft((i, j, k))
            elif arr[i][j][k] == 0:
                r += 1

day = 0
while r > 0:
    # print(q)
    nq = deque()
    while q:
        i, j, k = q.pop()
        for z, y, x in dirs:
            if i+z < 0 or i+z >= h or j+y < 0 or j+y >= n or k+x < 0 or k+x >= m:
                continue
            if arr[i+z][j+y][k+x] == 0:
                r -= 1
                arr[i+z][j+y][k+x] = 1
                nq.append((i+z, j+y, k+x))
    day += 1
    if r == 0:
        break
    # print(r)
    q = nq
    if not q:
        day = -1
        break
print(day)
