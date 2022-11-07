n, m = map(int, input().split())
g = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = set()
    if b not in g:
        g[b] = set()
    g[a].add(b)
    g[b].add(a)

vis = [False]*n
ans = 0


def dfs(i, count):
    global ans, vis
    # print(i, count, vis)
    if i not in g:
        return
    if ans >= 5:
        return
    ans = max(ans, count)
    for j in g[i]:
        if vis[j]:
            continue
        vis[j]=True
        dfs(j, count+1)
    if ans<5:
        vis[i]=False


for i in range(n):
    vis = [False]*n
    vis[i]=True
    dfs(i, 1)

if ans >= 5:
    print(1)
else:
    print(0)
