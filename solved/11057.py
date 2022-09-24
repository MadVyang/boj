n = int(input())
dp = []
for i in range(n+1):
    dp.append([0]*10)

for i in range(10):
    dp[1][i] = 1
# dp[1][0] = 1

for i in range(2, n+1):
    sm = 0
    for j in range(10):
        sm += dp[i-1][j]
        dp[i][j] = sm % 10007

print(sum(dp[n]) % 10007)
