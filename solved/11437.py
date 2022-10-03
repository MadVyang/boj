import sys
sys.setrecursionlimit(10**6)

n = int(input())
g = {}
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a not in g:
        g[a] = {}
    if b not in g:
        g[b] = {}
    g[a][b] = 0
    g[b][a] = 0

maxdepth = 30
parent = [[0]*(maxdepth+1) for i in range(n+1)]
depth = [0 for i in range(n+1)]


def dfs(i):
    for k in range(1, maxdepth+1):
        parent[i][k] = parent[parent[i][k-1]][k-1]

    for j in g[i]:
        if j != parent[i][0]:
            parent[j][0] = i
            depth[j] = depth[i]+1
            dfs(j)


dfs(1)


m = int(input())
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a==1 or b==1:
        print(1)
        continue
    if depth[a] > depth[b]:
        tmp = a
        a = b
        b = tmp

    if depth[a] != depth[b]:
        for i in range(maxdepth, -1, -1):
            if depth[parent[b][i]] >= depth[a]:
                b = parent[b][i]
    ret = a
    if a != b:
        for i in range(maxdepth, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
            ret = parent[a][i]
    print(ret)
