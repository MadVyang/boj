from math import inf, sqrt
import sys

input = sys.stdin.readline

n, ans = 0, inf
arr, used = [], []


def dfs(i, count):
    global n, ans
    if count == n//2:
        y, x = 0, 0
        # print(used)
        for k in range(n):
            if used[k] == 0:
                y += arr[k][0]
                x += arr[k][1]
            else:
                y -= arr[k][0]
                x -= arr[k][1]
        # print(y, x, sqrt(y*y+x*x))
        ans = min(ans, sqrt(y*y+x*x))
        return
    if i == n:
        return
    used[i] = 1
    dfs(i+1, count+1)
    used[i] = 0
    dfs(i+1, count)


t = int(input())
for _ in range(t):
    n = int(input())
    ans = inf
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    used = [0]*n
    dfs(0, 0)
    print(ans)
