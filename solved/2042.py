import sys


n, m, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

st = [0]*(n*4+1)


def init(s, e, n):
    if s == e:
        st[n] = arr[s]
    else:
        m = (s+e)//2
        st[n] = init(s, m, n*2)+init(m+1, e, n*2+1)
    return st[n]


def sum(s, e, n, l, r):
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return st[n]
    m = (s+e)//2
    return sum(s, m, n*2, l, r)+sum(m+1, e, n*2+1, l, r)


def update(s, e, n, i, d):
    if i < s or i > e:
        return
    st[n] += d
    if s == e:
        return
    m = (s+e)//2
    update(s, m, n*2, i, d)
    update(m+1, e, n*2+1, i, d)


init(0, n-1, 1)

for i in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        b -= 1
        update(0, n-1, 1, b, c-arr[b])
        arr[b] = c
    else:
        b -= 1
        c -= 1
        print(sum(0, n-1, 1, b, c))
