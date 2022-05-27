import heapq
import sys


n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip().split()])
arr.sort(key=lambda x: x[0])

bag = []
for i in range(k):
    bag.append(int(sys.stdin.readline().strip()))
bag.sort()


q = []
j = 0
ans = 0
for i in range(k):
    while j < n:
        if bag[i] >= arr[j][0]:
            heapq.heappush(q, -arr[j][1])
            j += 1
        else:
            break
    if q:
        ans += -heapq.heappop(q)
print(ans)
