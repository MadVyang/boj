import sys


n, m = map(int, input().split())
sm = set()
for i in range(m):
    sm.add(int(sys.stdin.readline().strip()))

dp = [[123456789]*200]
for i in range(n):
    dp.append([123456789]*200)

dp[1][1] = 0
for i in range(2, n+1):
    if i in sm:
        continue
    for j in range(1, min(i+1, 200)):
        for before_j in [j-1, j, j+1]:
            if 0 < before_j < 200 and i-before_j not in sm:
                dp[i][j] = min(dp[i][j], dp[i-before_j][before_j]+1)
    # print(i, min(dp[i]))

ans = min(dp[n])
if ans >= 123456789:
    ans = -1
print(ans)
# print(dp)
