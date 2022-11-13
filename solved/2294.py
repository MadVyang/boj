import sys


n, k = map(int, sys.stdin.readline().strip().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))
arr = list(set(arr))
arr.sort()
n = len(arr)
# print(arr)

# dp[i][j] = 현재 채운 돈 i, 마지막에 arr[j] 동전 사용
dp = []
for i in range(k+1):
    dp.append([123456789]*n)

for i in range(n):
    if arr[i]<=k:
        dp[arr[i]][i] = 1

for i in range(k+1):
    for j in range(n):
        if arr[j] > i:
            break
        for l in range(j+1):
            dp[i][j] = min(dp[i][j], dp[i-arr[j]][l]+1)

# print(dp)
ans = min(dp[k])
if ans >= 123456789:
    ans = -1
print(ans)
