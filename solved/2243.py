import sys


n = int(input())
tree = [0]*(4000005)


# def init(left, right, node):
#     if left == right:
#         tree[node] = 0
#         return
#     mid = (left+right)//2
#     init(left, mid, node*2)
#     init(mid+1, right, node*2+1)
#     tree[node] = 0


def update(left, right, node, index, value):
    if left > index or right < index:
        return
    # print(left, right, node, index, value)
    if left <= index <= right:
        tree[node] += value
        if left == right:
            return
    if left <= index or index <= right:
        mid = (left+right)//2
        update(left, mid, node*2, index, value)
        update(mid+1, right, node*2+1, index, value)


result = 0


def query(left, right, node, lidx, ridx):
    if left > ridx or right < lidx:
        return
    global result
    if lidx <= left and right <= ridx:
        result += tree[node]
        return
    mid = (left+right)//2
    query(left, mid, node*2, lidx, ridx)
    query(mid+1, right, node*2+1, lidx, ridx)


# init(1, 1000000, 1)

for _ in range(n):
    qr = [int(x) for x in sys.stdin.readline().strip().split()]
    if qr[0] == 1:
        low, high = 1, 1000000
        while low < high:
            mid = (low+high)//2
            result = 0
            query(1, 1000000, 1, 1, mid)
            if result < qr[1]:
                low = mid+1
            else:
                high = mid
        print(high)
        update(1, 1000000, 1, high, -1)
        pass
    else:
        update(1, 1000000, 1, qr[1], qr[2])
        pass
    # print(tree[:n])
