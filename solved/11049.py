n = int(input())
arr = []
dp = []
for _ in range(n):
    r, c = [int(x) for x in input().split()]
    arr.append([r, c])
    dp.append([0]*(n))

for k in range(1, n):
    for i in range(0, n-k):
        m = 2147483647
        for j in range(i, i+k):
            r = dp[i][j]+dp[j+1][i+k]+arr[i][0]*arr[j][1]*arr[i+k][1]
            if r < m:
                m = r
        dp[i][i+k] = m

print(dp[0][n-1])
