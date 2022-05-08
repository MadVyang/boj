from math import ceil
import sys


n = int(sys.stdin.readline().strip())
arr = [[int(x) for x in sys.stdin.readline().strip().split()] for i in range(n)]


def sim(m):
    cur = 0
    for a, b in arr:
        if a > 0:
            cur += a
        else:
            a = -a
            if cur-a < 0:
                tmp = (a-cur)
                cur += m*(tmp//m)
                if tmp % m > 0:
                    cur += m
            cur -= a
        # print(m, cur, a, b)
        if b != cur:
            return False
    return True


def gcd(m, n):
    while n != 0:
        t = m % n
        (m, n) = (n, t)
    return abs(m)


ch = False


def check():
    global ch
    pb = 0
    k = 0
    for a, b in arr:
        nk = b-(a+pb)
        pb = b
        if a > 0:
            continue
        if nk == 0:
            continue
        else:
            ch = True

        if k != 0:
            k = gcd(k, nk)
        else:
            k = nk
    return k


ans = check()
if not ch:
    ans = 1
if not sim(ans):
    ans = -1
print(ans)
