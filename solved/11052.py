n = int(input())
arr = [0]+[int(x) for x in input().split()]

dp = [0]*(n+1)
dp[1] = arr[1]

for i in range(2, n+1):
    dp[i] = arr[i]
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i-j]+dp[j])

print(dp[n])
