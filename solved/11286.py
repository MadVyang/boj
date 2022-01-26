import heapq
import sys

q = []
n = int(input())
l = {}
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            t = heapq.heappop(q)
            tt = heapq.heappop(l[t])
            print(tt)
    else:
        heapq.heappush(q, abs(x))
        if l.get(abs(x)) == None:
            l[abs(x)] = []
        heapq.heappush(l[abs(x)], x)
