import sys


n, m = map(int, input().split())
tree = [0]*n*4
lazy = [0]*n*4


def propagate(node, left, right):
    if lazy[node]:
        tree[node] = (right-left+1)-tree[node]
        if left != right:
            lazy[node*2] = 1-lazy[node*2]
            lazy[node*2+1] = 1-lazy[node*2+1]
        lazy[node] = 0


def update(node, left, right, lidx, ridx):
    propagate(node, left, right)
    if left > ridx or right < lidx:
        return
    if lidx <= left and right <= ridx:
        tree[node] = (right-left+1)-tree[node]
        if left != right:
            lazy[node*2] = 1-lazy[node*2]
            lazy[node*2+1] = 1-lazy[node*2+1]
        return
    mid = (left+right)//2
    update(node*2, left, mid, lidx, ridx)
    update(node*2+1, mid+1, right, lidx, ridx)
    tree[node] = tree[node*2]+tree[node*2+1]


result = 0


def query(node, left, right, lidx, ridx):
    global result
    propagate(node, left, right)
    if left > ridx or right < lidx:
        return
    if lidx <= left and right <= ridx:
        if tree[node]:
            result += tree[node]
        return
    mid = (left+right)//2
    query(node*2, left, mid, lidx, ridx)
    query(node*2+1, mid+1, right, lidx, ridx)


for i in range(m):
    o, s, t = [int(x) for x in sys.stdin.readline().strip().split()]
    if o == 0:
        update(1, 1, n, s, t)
    else:
        result = 0
        query(1, 1, n, s, t)
        print(result)
    # print(tree)
    # print(lazy)
