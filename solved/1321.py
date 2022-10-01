import sys


n = int(input())
arr = [0]+[int(x) for x in input().split()]

tree = [0]*(n*4)


def init(left, right, node):
    if left == right:
        tree[node] = arr[left]
        return
    mid = (left+right)//2
    init(left, mid, node*2)
    init(mid+1, right, node*2+1)
    tree[node] = tree[node*2]+tree[node*2+1]


def update(left, right, node, idx, value):
    if left > idx or right < idx:
        return
    if left <= idx and idx <= right:
        tree[node] += value
    if left==right:
        return
    mid = (left+right)//2
    update(left, mid, node*2, idx, value)
    update(mid+1, right, node*2+1, idx, value)


result = 0


def query(left, right, node, lidx, ridx):
    global result
    if left > ridx or right < lidx:
        return
    if lidx <= left and right <= ridx:
        result += tree[node]
        return
    mid = (left+right)//2
    query(left, mid, node*2, lidx, ridx)
    query(mid+1, right, node*2+1, lidx, ridx)


init(1, n, 1)
# print(tree)

m = int(input())
for _ in range(m):
    q = [int(x) for x in sys.stdin.readline().strip().split()]
    if q[0] == 1:
        update(1, n, 1, q[1], q[2])
    else:
        k = q[1]
        low, high = 1, n
        while low < high:
            mid = (low+high)//2
            result = 0
            query(1, n, 1, 1, mid)
            if result < k:
                low = mid+1
            else:
                high = mid
        print(high)
