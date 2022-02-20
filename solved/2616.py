n = int(input())
arr = [int(x) for x in input().split()]
k = int(input())

sum = [0]*n
ksum = 0
for i in range(k):
    ksum += arr[i]
for i in range(n-k):
    sum[i] = ksum
    ksum -= arr[i]
    ksum += arr[i+k]
sum[n-k] = ksum

dp = [[0]*n for i in range(4)]
mx = 0
mxs = [[0]*n for i in range(4)]
for i in range(n):
    dp[1][i] = sum[i]
    mx = max(mx, dp[1][i])
    mxs[1][i] = mx
mx = 0
for i in range(k, n):
    # mx = 0
    # for j in range(i-k+1):
    #     mx = max(mx, dp[1][j])
    dp[2][i] = mxs[1][i-k]+sum[i]
    mx = max(mx, dp[2][i])
    mxs[2][i] = mx
for i in range(k*2, n):
    # mx = 0
    # for j in range(i-k+1):
    #     mx = max(mx, dp[2][j])
    dp[3][i] = mxs[2][i-k]+sum[i]


mx = 0
for i in dp[3]:
    mx = max(mx, i)
print(mx)
# print(dp)
