from collections import deque
import heapq
import math
import sys


n, m = [int(x) for x in sys.stdin.readline().split()]
arr = []
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip()])


def bfs():
    q = [(0, 0, 0, False)]
    vis = []
    for i in range(n):
        vis.append([(math.inf)]*m)
    vis[0][0] = 0
    vis2 = []
    for i in range(n):
        vis2.append([(math.inf)]*m)
    vis2[0][0] = 0

    while q:
        c, i, j, b = heapq.heappop(q)
        # print(i, j, c)
        if i == n-1 and j == m-1:
            return c+1

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            y, x = i+di, j+dj
            if 0 <= y < n and 0 <= x < m and arr[y][x] == 0:
                if not b and vis[y][x] > c+1:
                    heapq.heappush(q, (c+1, y, x, b))
                    vis[y][x] = c+1
                if b and vis2[y][x] > c+1:
                    heapq.heappush(q, (c+1, y, x, b))
                    vis2[y][x] = c+1

        if not b:
            for di, dj in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
                y, x = i+di, j+dj
                if 0 <= y < n and 0 <= x < m and arr[y][x] == 0 and vis2[y][x] > c+2:
                    heapq.heappush(q, (c+2, y, x, True))
                    vis2[y][x] = c+2

    return math.inf


ans = bfs()


if ans == math.inf:
    ans = -1
print(ans)
