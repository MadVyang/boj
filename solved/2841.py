import heapq
import sys


n, p = map(int, input().split())
arrs = [[], [], [], [], [], [], []]
ans = 0
for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    while arrs[a] and -arrs[a][0] > b:
        ans += 1
        heapq.heappop(arrs[a])
    if not arrs[a] or (arrs[a] and -arrs[a][0] != b):
        ans += 1
        heapq.heappush(arrs[a], -b)

print(ans)
