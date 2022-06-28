t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    arr.append([int(x) for x in input().split()])
    arr.append([int(x) for x in input().split()])
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
        continue
    dp = [[0, 0] for i in range(n)]
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[1][0]

    dp[1][0] = arr[0][1]+arr[1][0]
    dp[1][1] = arr[1][1]+arr[0][0]

    for i in range(2, n):
        dp[i][0] = arr[0][i]+max(dp[i-1][1], dp[i-2][1])
        dp[i][1] = arr[1][i]+max(dp[i-1][0], dp[i-2][0])

    print(max(dp[n-1]))
