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
        st[n] = init(s, m, n*2)*init(m+1, e, n*2+1)
    st[n] %= 1000000007
    return st[n]


def sum(s, e, n, l, r):
    if l > e or r < s:
        return 1
    if l <= s and e <= r:
        return st[n]
    m = (s+e)//2
    r = sum(s, m, n*2, l, r)*sum(m+1, e, n*2+1, l, r)
    r %= 1000000007
    return r


def update(s, e, n, i, orig, new):
    if i < s or i > e:
        return st[n]
    if s == e:
        st[n] = new
    else:
        m = (s+e)//2
        st[n] = update(s, m, n*2, i, orig, new)*update(m+1, e, n*2+1, i, orig, new)
    st[n] %= 1000000007
    return st[n]


init(0, n-1, 1)
# print(st)

for i in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        b -= 1
        update(0, n-1, 1, b, arr[b], c)
        arr[b] = c
        # print(st)
    else:
        b -= 1
        c -= 1
        print(sum(0, n-1, 1, b, c))
