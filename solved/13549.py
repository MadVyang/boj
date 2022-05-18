import heapq
import math


n, k = map(int, input().split())
q = [(0, n)]
vis = [math.inf]*200002
vis[n]=0
while q:
    t, i = heapq.heappop(q)
    if i == k:
        break
    nexts = [(t+1, i+1), (t+1, i-1), (t, i*2)]
    for tt, ii in nexts:
        if ii > 200000 or ii < 0 or vis[ii]<=tt:
            continue
        vis[ii] = tt
        heapq.heappush(q, (tt, ii))

print(t)
