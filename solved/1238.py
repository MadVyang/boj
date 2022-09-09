import heapq
import math


n, m, x = [int(x) for x in input().split()]
g = {
    i+1: {} for i in range(n)
}
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    g[a][b] = c


d1 = {
    i+1: math.inf for i in range(n)
}
d1[x] = 0

q = []
heapq.heappush(q, (0, x))
while q:
    dis, i = heapq.heappop(q)
    if dis > d1[i]:
        continue
    for j in g[i]:
        if d1[j] > d1[i]+g[i][j]:
            d1[j] = d1[i]+g[i][j]
            heapq.heappush(q, (d1[j], j))

d2 = {
    i+1: math.inf for i in range(n)
}
d2[x] = 0

q = []
heapq.heappush(q, (0, x))
while q:
    dis, i = heapq.heappop(q)
    if dis > d2[i]:
        continue
    for j in range(1, n+1):
        if i in g[j] and d2[j] > d2[i]+g[j][i]:
            d2[j] = d2[i]+g[j][i]
            heapq.heappush(q, (d2[j], j))

mx = 0
for i in range(1, n+1):
    mx = max(mx, d1[i]+d2[i])
print(mx)
