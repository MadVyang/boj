n, k = [int(x) for x in input().split()]
w = [0]
v = [0]
for _ in range(n):
    _w, _v = [int(x) for x in input().split()]
    w.append(_w)
    v.append(_v)

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif w[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w[i]]+v[i], dp[i-1][j])
print(dp[n][k])
# print(dp)
