while True:
    n = int(input())
    if n == -1:
        break
    dp = [([0]*n) for x in range(n)]
    arr = []
    for i in range(n):
        arr.append([int(x) for x in input().split()])
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                continue
            if i+arr[i][j] < n:
                dp[i+arr[i][j]][j] += dp[i][j]
            if j+arr[i][j] < n:
                dp[i][j+arr[i][j]] += dp[i][j]
    print(dp[n-1][n-1])
    break
