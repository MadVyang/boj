import heapq
import math

n, t = [int(x) for x in input().split()]
arr = [[int(x) for x in input().split()] for _ in range(n)]

d = [[[math.inf]*3 for _ in range(n)] for _ in range(n)]
v = [[[False]*3 for _ in range(n)] for _ in range(n)]

d[0][0][0] = 0

q = []
heapq.heappush(q, (0, 0, 0, 0))


def get_closest_unvisited():

    return heapq.heappop(q)

    cur_dis = math.inf
    ri = -1
    rj = -1
    rk = -1
    for i in range(n):
        for j in range(n):
            for k in range(3):
                if not v[i][j][k] and cur_dis >= d[i][j][k]:
                    ri = i
                    rj = j
                    rk = k
                    cur_dis = d[i][j][k]
    return (ri, rj, rk)


while len(q) > 0:
    _, i, j, k = get_closest_unvisited()
    if v[i][j][k]:
        continue
    v[i][j][k] = True
    kp1 = (k+1) % 3
    r = 0
    if i > 0:
        if k % 3 == 2:
            r = arr[i-1][j]
        if d[i-1][j][kp1] > d[i][j][k]+t+r:
            d[i-1][j][kp1] = d[i][j][k]+t+r
            heapq.heappush(q, (d[i-1][j][kp1], i-1, j, kp1))
    if i < n-1:
        if k % 3 == 2:
            r = arr[i+1][j]
        if d[i+1][j][kp1] > d[i][j][k]+t+r:
            d[i+1][j][kp1] = d[i][j][k]+t+r
            heapq.heappush(q, (d[i+1][j][kp1], i+1, j, kp1))
    if j > 0:
        if k % 3 == 2:
            r = arr[i][j-1]
        if d[i][j-1][kp1] > d[i][j][k]+t+r:
            d[i][j-1][kp1] = d[i][j][k]+t+r
            heapq.heappush(q, (d[i][j-1][kp1], i, j-1, kp1))
    if j < n-1:
        if k % 3 == 2:
            r = arr[i][j+1]
        if d[i][j+1][kp1] > d[i][j][k]+t+r:
            d[i][j+1][kp1] = d[i][j][k]+t+r
            heapq.heappush(q, (d[i][j+1][kp1], i, j+1, kp1))

print(min(d[n-1][n-1]))
