from collections import deque
import sys


n = int(input())
q = deque()
ans = 0
for i in range(n):
    k = int(sys.stdin.readline().strip())
    while q and q[-1][0] <= k:
        h, idx = q.pop()
        ans += i-idx-1
    q.append((k, i))
    # print(i, ans)
for h, idx in q:
    ans += q[-1][1]-idx
print(ans)
