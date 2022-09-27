import sys


n = int(input())
arr = [0]+[int(x) for x in input().split()]
tree = [(0, 0)]*(n*4)


def init(left, right, node):
    if left == right:
        tree[node] = (arr[left], left)
        return
    mid = (left+right)//2
    init(left, mid, node*2)
    init(mid+1, right, node*2+1)
    tree[node] = min(tree[node*2], tree[node*2+1])


def update(left, right, node, idx, value):
    if left > idx or right < idx:
        return
    if left == right:
        arr[idx] = value
        tree[node] = (value, idx)
        return
    mid = (left+right)//2
    update(left, mid, node*2, idx, value)
    update(mid+1, right, node*2+1, idx, value)
    tree[node] = min(tree[node*2], tree[node*2+1])


ans = (0, 0)


def query(left, right, node, lidx, ridx):
    if lidx > right or ridx < left:
        return
    if lidx <= left and right <= ridx:
        global ans
        ans = min(ans, tree[node])
        return
    mid = (left+right)//2
    query(left, mid, node*2, lidx, ridx)
    query(mid+1, right, node*2+1, lidx, ridx)


init(1, n, 1)
# print(tree)

m = int(input())
for _ in range(m):
    qr = [int(x) for x in sys.stdin.readline().strip().split()]
    if qr[0] == 1:
        update(1, n, 1, qr[1], qr[2])
    else:
        ans = (sys.maxsize, sys.maxsize)
        query(1, n, 1, 1, n)
        print(ans[1])
