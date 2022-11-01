n, l, r = map(int, input().split())

dp = []
for i in range(n+1):
    dp.append([])
    for j in range(n+1):
        dp[i].append([0]*(n+1))

dp[1][1][1] = 1
if n>1:
    dp[2][2][1] = 1
    dp[2][1][2] = 1
    for i in range(3, n+1):
        for j in range(1, i+1):
            for k in range(1, i+1):
                dp[i][j][k] = (dp[i-1][j-1][k]+dp[i-1][j][k-1]+dp[i-1][j][k]*(i-2)) % 1000000007

# print(dp[n])
print(dp[n][l][r])
