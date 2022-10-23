import sys


n = int(input())
arr = [0]+[int(x) for x in input().split()]
m = int(input())

tree = [0]*(n*4)


def init(node, left, right):
    if left == right:
        tree[node] = arr[left]
        return
    mid = (left+right)//2
    init(node*2, left, mid)
    init(node*2+1, mid+1, right)


init(1, 1, n)

lazy = [0]*(n*4)


def propagate(node, left, right):
    if lazy[node] != 0:
        if left == right:
            tree[node] ^= lazy[node]
        else:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        lazy[node] = 0


def update(node, left, right, lidx, ridx, val):
    # print(node, left, right, lidx, ridx, val)
    propagate(node, left, right)
    if left > ridx or right < lidx:
        return
    if lidx <= left and right <= ridx:
        if left == right:
            tree[node] ^= val
        else:
            lazy[node*2] ^= val
            lazy[node*2+1] ^= val
        return
    mid = (left+right)//2
    update(node*2, left, mid, lidx, ridx, val)
    update(node*2+1, mid+1, right, lidx, ridx, val)


def query(node, left, right, idx):
    propagate(node, left, right)
    if left > idx or right < idx:
        return
    if left == right:
        print(tree[node])
        return
    mid = (left+right)//2
    query(node*2, left, mid, idx)
    query(node*2+1, mid+1, right, idx)


for i in range(m):
    qr = [int(x) for x in sys.stdin.readline().split()]
    if qr[0] == 1:
        update(1, 1, n, qr[1]+1, qr[2]+1, qr[3])
        # print(tree)
        # print(lazy)
    else:
        query(1, 1, n, qr[1]+1)
