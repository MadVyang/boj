import sys


n, m = map(int, input().split())
arr = [[0]*(n+1)]
for i in range(n):
    t = [0]+[int(x) for x in sys.stdin.readline().strip().split()]
    arr.append(t)

dp = []
for i in range(n+1):
    dp.append([0]*(n+1))
dp[1][1] = arr[1][1]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            continue
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+arr[i][j]
# print(dp)


def solve(x1, y1, x2, y2):
    return dp[y2][x2]-dp[y1-1][x2]-dp[y2][x1-1]+dp[y1-1][x1-1]


for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    print(solve(y1, x1, y2, x2))
