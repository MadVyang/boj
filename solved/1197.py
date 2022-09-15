import sys


v, e = map(int, input().split())
g = {}
edges = []
root = [i for i in range(v+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a not in g:
        g[a] = {}
    if b not in g:
        g[b] = {}
    g[a][b] = c
    g[b][a] = c

    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])


def find(i):
    if i != root[i]:
        root[i] = find(root[i])
    return root[i]


count = 0
ans = 0
for i in range(e):
    a, b, c = edges[i]
    ra, rb = find(a), find(b)
    if ra != rb:
        if ra > rb:
            root[ra] = rb
        else:
            root[rb] = ra
        ans += c
        count += 1
        if count == v-1:
            break

print(ans)
