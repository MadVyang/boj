n = int(input())
m = int(input())
g = []
for i in range(n):
    g.append([int(x) for x in input().split()])
arr = [int(x)-1 for x in input().split()]

root = [i for i in range(n)]


def find(i):
    if root[i] != i:
        root[i] = find(root[i])
    return root[i]


def union(i, j):
    ri, rj = find(i), find(j)
    if ri > rj:
        root[ri] = root[rj]
    else:
        root[rj] = root[ri]


for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            union(i, j)

ans = 'YES'
for i in range(1, m):
    if find(arr[i-1]) != find(arr[i]):
        ans = 'NO'
        break
print(ans)
