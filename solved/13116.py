import sys


def f(n):
    s = set()
    while n:
        s.add(n)
        n //= 2
    return s


t = int(input())
for _ in range(t):
    a, b = sys.stdin.readline().strip().split()
    a, b = int(a), int(b)
    sa, sb = f(a), f(b)
    print(max(sa & sb)*10)
