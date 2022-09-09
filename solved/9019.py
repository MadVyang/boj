from collections import deque
import sys


ops = 'DSLR'


def op(n, p):
    if p == 'D':
        n = n*2 % 10000
    elif p == 'S':
        n = (n-1) % 10000
    elif p == 'L':
        n = (n % 1000)*10 + n//1000
    else:
        n = n//10 + n % 10*1000
    return n


# for p in ops:
#     print(op(1234, p))


t = int(input())
for _ in range(t):
    a, b = sys.stdin.readline().strip().split()
    a, b = int(a), int(b)

    vis = set([a])
    q = deque([(a, '')])
    while q:
        c, cp = q.popleft()
        if c == b:
            print(cp)
            solved = True
            break
        for p in ops:
            nc = op(c, p)
            if nc in vis:
                continue
            vis.add(nc)
            q.append((nc, cp+p))
