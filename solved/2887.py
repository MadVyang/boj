import sys


n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip().split()])

arr.sort(key=lambda x: x[0])
for i in range(n):
    arr[i].append(i)


def cost(a, b):
    return min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))


edges = []


def fill_edges():
    for i in range(1, n):
        id0, id1 = arr[i-1][-1], arr[i][-1]
        c = cost(arr[i-1], arr[i])
        edges.append([id0, id1, c])


fill_edges()
arr.sort(key=lambda x: x[1])
fill_edges()
arr.sort(key=lambda x: x[2])
fill_edges()

edges.sort(key=lambda x: x[2])


root = [i for i in range(n)]


def find(a):
    if root[a] == a:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        root[a] = b
    else:
        root[b] = a


ans = 0
for edge in edges:
    i, j, c = edge
    if find(i) == find(j):
        continue
    union(i, j)
    ans += c

print(ans)
