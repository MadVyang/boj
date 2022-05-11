import heapq
import sys


n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip().split()])
arr.sort(key=lambda x: (x[0], x[1]))

rooms = [-1]
ans = 1
for i in range(n):
    a, b = arr[i]
    if rooms[0] <= a:
        heapq.heappop(rooms)
    else:
        ans += 1
    heapq.heappush(rooms, b)
print(ans)
