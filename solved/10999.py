import sys


n, m, k = map(int, input().split())
tree = [0]*(4*n)
lazy = [0]*(4*n)
arr = [0]*(n+1)


def init(node, left, right):
    if left == right:
        tree[node] = arr[left]
        return
    mid = (left+right)//2
    init(node*2, left, mid)
    init(node*2+1, mid+1, right)
    tree[node] = tree[node*2]+tree[node*2+1]


def lazy_propagate(node, left, right):
    if lazy[node] != 0:
        tree[node] += lazy[node]*(right-left+1)
        if left != right:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0


def update(node, left, right, lidx, ridx, val):
    lazy_propagate(node, left, right)
    if left > ridx or lidx > right:
        return
    if lidx <= left and right <= ridx:
        tree[node] += val*(right-left+1)
        if left != right:
            lazy[node*2] += val
            lazy[node*2+1] += val
        return
    mid = (left+right)//2
    update(node*2, left, mid, lidx, ridx, val)
    update(node*2+1, mid+1, right, lidx, ridx, val)
    tree[node] = tree[node*2]+tree[node*2+1]


result = 0


def query(node, left, right, lidx, ridx):
    lazy_propagate(node, left, right)
    global result
    if left > ridx or lidx > right:
        return
    if lidx <= left and right <= ridx:
        result += tree[node]
        return
    mid = (left+right)//2
    query(node*2, left, mid, lidx, ridx)
    query(node*2+1, mid+1, right, lidx, ridx)


for i in range(1, n+1):
    arr[i] = int(sys.stdin.readline().strip())

init(1, 1, n)

for i in range(m+k):
    q = [int(x) for x in sys.stdin.readline().strip().split()]
    if q[0] == 1:
        update(1, 1, n, q[1], q[2], q[3])
    else:
        result = 0
        query(1, 1, n, q[1], q[2])
        print(result)
