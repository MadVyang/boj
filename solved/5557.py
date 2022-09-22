from collections import deque


n = int(input())
arr = [int(x) for x in input().split()]
last = arr[-1]
q = deque([(arr[0], 0)])
mem = {(arr[0], 0): 1}
arr = arr[1:-1]
ans = 0
while q:
    cur, idx = q.popleft()
    if idx == len(arr):
        if cur == last:
            ans += mem[(cur, idx)]
        continue
    
    for next in [cur+arr[idx], cur-arr[idx]]:
        if 0 <= next <= 20:
            if (next, idx+1) not in mem:
                mem[(next, idx+1)] = 0
                q.append((next, idx+1))
            mem[(next, idx+1)] += mem[(cur, idx)]
print(ans)
