from queue import PriorityQueue
import heapq
import sys

q = []
n = int(sys.stdin.readline())
for i in range(n):
    values = [int(x) for x in sys.stdin.readline().split()]
    a = values[0]
    if a == 0:
        if len(q) == 0:
            print(-1)
        else:
            print(-heapq.heappop(q))
    else:
        for j in range(a):
            heapq.heappush(q, -values[j+1])
