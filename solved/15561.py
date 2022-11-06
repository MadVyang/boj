from cmath import inf
import sys


n, q, u, v = map(int, input().split())
arr = [0]+[int(x) for x in input().split()]
for i in range(1, n+1):
    arr[i] = arr[i]*u+v


class Node:
    def __init__(self, sum, lmx, rmx, mx):
        self.sum = sum
        self.lmx = lmx
        self.rmx = rmx
        self.mx = mx

    def __add__(self, value):
        self.sum += value
        self.lmx += value
        self.rmx += value
        self.mx += value
        return self


tree = [Node(0, 0, 0, 0) for i in range(n*4)]


def merge(a: Node, b: Node) -> Node:
    c = Node(0, 0, 0, 0)
    c.sum = a.sum+b.sum
    c.lmx = max(a.lmx, a.sum+b.lmx)
    c.rmx = max(b.rmx, b.sum+a.rmx)
    c.mx = max(a.mx, b.mx, a.rmx+b.lmx)
    return c


def init(node, left, right):
    if left == right:
        tree[node] = Node(arr[left], arr[left], arr[left], arr[left])
        return
    mid = (left+right)//2
    init(node*2, left, mid)
    init(node*2+1, mid+1, right)
    tree[node] = merge(tree[node*2], tree[node*2+1])


def update(node, left, right, idx, v):
    if idx < left or idx > right:
        return
    if left == right:
        tree[node] += v
        return
    mid = (left+right)//2
    update(node*2, left, mid, idx, v)
    update(node*2+1, mid+1, right, idx, v)
    tree[node] = merge(tree[node*2], tree[node*2+1])


def query(node, left, right, lidx, ridx):
    if ridx < left or lidx > right:
        return Node(0, -inf, -inf, -inf)
    if lidx <= left and right <= ridx:
        return tree[node]
    mid = (left+right)//2
    return merge(
        query(node*2, left, mid, lidx, ridx),
        query(node*2+1, mid+1, right, lidx, ridx)
    )


init(1, 1, n)
for i in range(q):
    c, a, b = map(int, sys.stdin.readline().strip().split())
    if c == 0:
        query(1, 1, n, a, b)
        print(query(1, 1, n, a, b).mx-v)
    else:
        update(1, 1, n, a, u*b+v-arr[a])
        arr[a] = u*b+v
