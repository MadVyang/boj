import sys

f = [1]*4000005
for i in range(2, 4000001):
    f[i] = (f[i-1]*i) % 1000000007


def pow(a, b):
    if b == 0:
        return 1
    tmp = pow(a, b//2)
    tmp *= tmp
    if b % 2 == 1:
        tmp *= a
    tmp %= 1000000007
    return tmp


def sol(n, k):
    tmp = f[n-k]*f[k] % 1000000007
    tmp = pow(tmp, 1000000005)
    return f[n]*tmp % 1000000007


m = int(input())
for i in range(m):
    n, k = map(int, sys.stdin.readline().strip().split())

    print(sol(n, k))
