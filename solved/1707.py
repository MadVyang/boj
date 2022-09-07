import sys


sys.setrecursionlimit(10**6)

k = int(sys.stdin.readline().strip())
r = True
for _ in range(k):
    v, e = map(int, sys.stdin.readline().strip().split())
    g = {}
    for i in range(e):
        a, b = map(int, sys.stdin.readline().strip().split())
        if a not in g:
            g[a] = set()
        if b not in g:
            g[b] = set()
        g[a].add(b)
        g[b].add(a)

    color = {}
    r = True

    def dfs(i, c):
        # print(i, c)
        global r
        if not r:
            return
        if i in color:
            if color[i] != c:
                r = False
            return
        color[i] = c
        if i not in g:
            return
        for j in g[i]:
            dfs(j, 1-c)

    for i in range(1, v+1):
        if i not in color:
            dfs(i, 0)
            if not r:
                break

    if r:
        print('YES')
    else:
        print('NO')
