import heapq
import sys


n, m = map(int, input().split())
arr = [0]+[int(x) for x in input().split()]
g = {}
for i in range(m):
    a, b, c = [int(x) for x in sys.stdin.readline().strip().split()]
    if a not in g:
        g[a] = {}
    if b not in g:
        g[b] = {}
    g[a][b] = c
    g[b][a] = c

q = [(0, 1, arr[1])]
cost_vis = [123456789]*(n+1)
cheapest_vis = [123456789]*(n+1)
cost_vis[1] = 0
cheapest_vis[1] = arr[1]
while q:
    cost, idx, cheapest = heapq.heappop(q)
    if cost_vis[idx] < cost and cheapest_vis[idx] < cheapest:
        continue
    if idx == n:
        print(cost)
        break
    for i in g[idx]:
        n_cost = cost+g[idx][i]*cheapest
        n_cheapest = min(cheapest, arr[i])
        if n_cost < cost_vis[i] or n_cheapest < cheapest_vis[i]:
            heapq.heappush(q, (n_cost, i, n_cheapest))
            # print(cost, idx, cheapest, q)
            cost_vis[i] = n_cost
            cheapest_vis[i] = n_cheapest
