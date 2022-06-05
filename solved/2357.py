import math
import sys


n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))


st = [(0, 0)]*(n*4)


def init(n, s, e):
    if s == e:
        st[n] = (arr[s], arr[s])
    else:
        m = (s+e)//2
        a, b = init(n*2, s, m)
        c, d = init(n*2+1, m+1, e)
        st[n] = (max(a, c), min(b, d))
    return st[n]


def get(n, s, e, l, r):
    if l > e or r < s:
        return (-1, math.inf)
    if l <= s and e <= r:
        return st[n]
    m = (s+e)//2
    a, b = get(n*2, s, m, l, r)
    c, d = get(n*2+1, m+1, e, l, r)
    return (max(a, c), min(b, d))


init(1, 0, n-1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    mx, mn = get(1, 0, n-1, a-1, b-1)
    print(mn, mx)
