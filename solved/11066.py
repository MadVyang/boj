t = int(input())
for _ in range(t):
    k = int(input())
    arr = [int(x) for x in input().split()]
    dp = [[0]*k for x in range(k)]
    sum = [0]*k
    sum[0] = arr[0]

    for i in range(k-1):
        sum[i+1] = sum[i]+arr[i+1]
        dp[i][i+1] = arr[i]+arr[i+1]
    for c in range(2, k):
        for i in range(k-c):
            x = i+c
            mn = 10000*1000*1000
            for j in range(c):
                r = dp[i][i+j]+dp[i+j+1][x]+sum[x]-sum[i]+arr[i]
                mn = min(mn, r)
            dp[i][x] = mn
    print(dp[0][k-1])
