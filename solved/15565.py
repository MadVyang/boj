from collections import deque


n,k=map(int,input().split())
arr = [int(x) for x in input().split()]
dq = deque()
ans = 123456789
for i in range(n):
    if arr[i]==1:
        if len(dq)==k:
            dq.popleft()
        dq.append(i)
        if len(dq)==k:
            ans = min(ans, i-dq[0]+1)

if ans==123456789:
    ans=-1
print(ans)