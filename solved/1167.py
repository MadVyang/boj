import sys


v = int(input())
tree = [{} for i in range(v)]
for i in range(v):
    tmp = [int(x) for x in sys.stdin.readline().strip().split()]
    for j in range(1, len(tmp)-1, 2):
        tree[tmp[0]-1][tmp[j]-1] = tmp[j+1]

vis = [False]*v
vis[0] = True


def dfs(i):
    mx, k = 0, i
    for j in tree[i]:
        if not vis[j]:
            vis[j] = True
            _mx, _k = dfs(j)
            if _mx+tree[i][j] > mx:
                mx = _mx+tree[i][j]
                k = _k
            vis[j] = False
    return mx, k


mx, k = dfs(0)
# print(mx, k)
vis = [False]*v
vis[k] = True
mx, _ = dfs(k)
print(mx)
