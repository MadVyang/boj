from collections import deque
import sys


n = int(input())
arr = [0]*(n+1)
arr[1] = 1
qs = {}
for _ in range(n-1):
    a, b = [int(x) for x in sys.stdin.readline().strip().split()]
    if a not in qs:
        qs[a] = set()
    qs[a].add(b)
    if b not in qs:
        qs[b] = set()
    qs[b].add(a)

q = deque()
q.appendleft(1)
while q:
    p = q.pop()
    for i in qs[p]:
        if arr[i] == 0:
            arr[i] = p
            q.appendleft(i)

for i in range(2, n+1):
    print(arr[i])
