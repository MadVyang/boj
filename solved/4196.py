from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())

    g = {}
    ig = {}
    scc = [0]*(n+1)

    for i in range(m):
        x, y = map(int, input().strip().split())
        if x not in g:
            g[x] = set()
        if y not in ig:
            ig[y] = set()
        g[x].add(y)
        ig[y].add(x)

    st = deque()
    vis = [False]*(n+1)

    def dfs1(i):
        if i in g:
            for j in g[i]:
                if not vis[j]:
                    vis[j] = True
                    dfs1(j)
        st.append(i)

    for i in range(1, n+1):
        if vis[i]:
            continue
        vis[i] = True
        dfs1(i)

    st2 = deque()
    vis = [False]*(n+1)

    def dfs2(i):
        if i in ig:
            for j in ig[i]:
                if not vis[j]:
                    vis[j] = True
                    dfs2(j)
        st2.append(i)

    sccn = 0
    while st:
        i = st.pop()
        if vis[i]:
            continue
        vis[i] = True
        st2.clear()
        dfs2(i)
        for j in st2:
            scc[j] = sccn
        sccn += 1

    gg = {}
    for i in range(1, n+1):
        if i not in g:
            continue
        for j in g[i]:
            if scc[j] == scc[i]:
                continue
            if scc[i] not in gg:
                gg[scc[i]] = set()
            gg[scc[i]].add(scc[j])

    indegree = [0]*sccn
    ans = 0
    for i in range(sccn):
        if i in gg:
            for j in gg[i]:
                indegree[j] += 1
    for i in range(sccn):
        if indegree[i] == 0:
            ans += 1
    print(ans)
