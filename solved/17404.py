import math


ans = math.inf
n = int(input())
ex = []
for i in range(n):
    ex.append([int(x) for x in input().split()])

dp = [[math.inf]*n, [math.inf]*n, [math.inf]*n]
dp[0][0] = ex[0][0]
for i in range(1, n-1):
    dp[0][i] = ex[i][0]+min(dp[1][i-1], dp[2][i-1])
    dp[1][i] = ex[i][1]+min(dp[0][i-1], dp[2][i-1])
    dp[2][i] = ex[i][2]+min(dp[0][i-1], dp[1][i-1])
dp[1][n-1] = ex[n-1][1]+min(dp[0][n-2], dp[2][n-2])
dp[2][n-1] = ex[n-1][2]+min(dp[0][n-2], dp[1][n-2])
ans = min(ans, dp[1][n-1], dp[2][n-1])

dp = [[math.inf]*n, [math.inf]*n, [math.inf]*n]
dp[1][0] = ex[0][1]
for i in range(1, n-1):
    dp[0][i] = ex[i][0]+min(dp[1][i-1], dp[2][i-1])
    dp[1][i] = ex[i][1]+min(dp[0][i-1], dp[2][i-1])
    dp[2][i] = ex[i][2]+min(dp[0][i-1], dp[1][i-1])
dp[0][n-1] = ex[n-1][0]+min(dp[1][n-2], dp[2][n-2])
dp[2][n-1] = ex[n-1][2]+min(dp[0][n-2], dp[1][n-2])
ans = min(ans, dp[0][n-1], dp[2][n-1])

dp = [[math.inf]*n, [math.inf]*n, [math.inf]*n]
dp[2][0] = ex[0][2]
for i in range(1, n-1):
    dp[0][i] = ex[i][0]+min(dp[1][i-1], dp[2][i-1])
    dp[1][i] = ex[i][1]+min(dp[0][i-1], dp[2][i-1])
    dp[2][i] = ex[i][2]+min(dp[0][i-1], dp[1][i-1])
dp[0][n-1] = ex[n-1][0]+min(dp[1][n-2], dp[2][n-2])
dp[1][n-1] = ex[n-1][1]+min(dp[0][n-2], dp[2][n-2])
ans = min(ans, dp[0][n-1], dp[1][n-1])

print(ans)
