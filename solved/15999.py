import sys


n, m = [int(x) for x in input().split()]
arr = [sys.stdin.readline().strip() for i in range(n)]

ans = 1
for i in range(n):
    for j in range(m):
        cur = arr[i][j]
        if i-1 >= 0 and arr[i-1][j] != cur:
            continue
        if j-1 >= 0 and arr[i][j-1] != cur:
            continue
        if i+1 < n and arr[i+1][j] != cur:
            continue
        if j+1 < m and arr[i][j+1] != cur:
            continue
        ans *= 2
        ans %= 1000000007

print(ans)
