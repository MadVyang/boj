import sys


n = int(input())

tree = [0]*2000001*4


def insert(left, right, node, idx):
    if left == right:
        tree[node] += 1
        return
    mid = (left+right)//2
    if left <= idx <= mid:
        insert(left, mid, node*2, idx)
    if mid+1 <= idx <= right:
        insert(mid+1, right, node*2+1, idx)
    tree[node] = tree[node*2]+tree[node*2+1]


result = 0


def delete(left, right, node, rank):
    if left == right:
        global result
        result = left
        tree[node] -= 1
        return
    mid = (left+right)//2
    if tree[node*2] >= rank:
        delete(left, mid, node*2, rank)
    else:
        delete(mid+1, right, node*2+1, rank-tree[node*2])
    tree[node] = tree[node*2]+tree[node*2+1]


for _ in range(n):
    t, x = map(int, sys.stdin.readline().strip().split())
    if t == 1:
        insert(1, 2000000, 1, x)
    else:
        delete(1, 2000000, 1, x)
        print(result)
