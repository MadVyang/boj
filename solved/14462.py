import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().strip()


n = int(input())
ls = [int(input()) for _ in range(n)]
rs = [int(input()) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
vs = [[False]*n for _ in range(n)]


def dfs(i, j):
    if i == n or j == n:
        return 0
    if vs[i][j]:
        return dp[i][j]
    mx = max(dfs(i+1, j), dfs(i, j+1))
    if abs(ls[i]-rs[j]) <= 4:
        mx = max(mx, dfs(i+1, j+1)+1)
    dp[i][j] = mx
    vs[i][j] = True
    return dp[i][j]


print(dfs(0, 0))
