import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [[x for x in input()] for i in range(n)]
vis = [[False]*n for i in range(n)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(i, j, c):
    if i < 0 or i >= n or j < 0 or j >= n:
        return
    if arr[i][j] != c:
        return
    if vis[i][j]:
        return
    vis[i][j] = True
    for y, x in dirs:
        dfs(i+y, j+x, c)


count = 0
for i in range(n):
    for j in range(n):
        if not vis[i][j]:
            count += 1
            dfs(i, j, arr[i][j])


vis = [[False]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

count2 = 0
for i in range(n):
    for j in range(n):
        if not vis[i][j]:
            count2 += 1
            dfs(i, j, arr[i][j])

print(count, count2)
