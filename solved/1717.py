import sys
sys.setrecursionlimit(10**6)


n, m = map(int, sys.stdin.readline().strip().split())

root = [i for i in range(n+1)]


def find(i):
    if root[i] == i:
        return i
    root[i] = find(root[i])
    return root[i]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b


for i in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print('yes')
        else:
            print('no')
