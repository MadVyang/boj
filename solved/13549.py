from collections import deque
import math


n, k = map(int, input().split())
q = deque([(0, n)])
vis = [math.inf]*200002
vis[n] = 0
while q:
    t, i = q.pop()
    if i == k:
        break

    nexts = [(t+1, i+1), (t+1, i-1), (t, i*2)]
    for tt, ii in nexts:
        if ii > 200000 or ii < 0 or vis[ii] <= tt:
            continue
        vis[ii] = tt
        if tt == t:
            q.append((tt, ii))
        else:
            q.appendleft((tt, ii))

print(t)
