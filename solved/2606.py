n = int(input())
m = int(input())
arr = [[False]*(n+1) for i in range(n+1)]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    arr[a][b] = True
    arr[b][a] = True

vis = [False]*(n+1)


def dfs(i):
    if vis[i]:
        return
    vis[i] = True
    for j in range(1, n+1):
        if arr[i][j]:
            dfs(j)


dfs(1)

count = 0
for i in range(n):
    if vis[i+1]:
        count += 1

print(count-1)
