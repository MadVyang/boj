n = int(input())
pan = [[int(x) for x in input().split()] for i in range(n)]

dp = [[], [], []]
dp[0] = [[0]*n for i in range(n)]
dp[1] = [[0]*n for i in range(n)]
dp[2] = [[0]*n for i in range(n)]
dp[0][0][1] = 1

for i in range(n):
    for j in range(n):
        if pan[i][j] == 1:
            continue

        if j > 0:
            dp[0][i][j] += dp[0][i][j-1]
            dp[0][i][j] += dp[2][i][j-1]

        if i > 0:
            dp[1][i][j] += dp[1][i-1][j]
            dp[1][i][j] += dp[2][i-1][j]

        if i == 0 or j == 0 or pan[i-1][j] == 1 or pan[i][j-1] == 1:
            continue
        dp[2][i][j] += dp[0][i-1][j-1]+dp[1][i-1][j-1]+dp[2][i-1][j-1]

# print(dp[0][n-1][n-1], dp[1][n-1][n-1], dp[2][n-1][n-1])
print(dp[0][n-1][n-1]+dp[1][n-1][n-1]+dp[2][n-1][n-1])
