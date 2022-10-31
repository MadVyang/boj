import sys


n, k = map(int, input().split())
tree = [0]*(n*4)


def init(node, left, right):
    if left == right:
        tree[node] = 1
        return
    mid = (left+right)//2
    init(node*2, left, mid)
    init(node*2+1, mid+1, right)
    tree[node] = tree[node*2]+tree[node*2+1]


init(1, 1, n)

ans = []


def delete(node, left, right, x):
    if left == right:
        tree[node] -= 1
        ans.append(left)
        return
    mid = (left+right)//2
    if x <= tree[node*2]:
        delete(node*2, left, mid, x)
    else:
        delete(node*2+1, mid+1, right, x - tree[node*2])
    tree[node] = tree[node*2]+tree[node*2+1]


cur = k
for i in range(n):
    delete(1, 1, n, cur)
    # print(cur)
    if i < n-1:
        cur = (cur+k-2) % (n-i-1)+1

print('<'+', '.join([str(x) for x in ans])+'>')
