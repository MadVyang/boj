import sys


def input():
    return sys.stdin.readline().strip()


t = int(input())
n = int(input())
al = [int(x) for x in input().split()]
al.insert(0, 0)
m = int(input())
bl = [int(x) for x in input().split()]
bl.insert(0, 0)

a_acum = [0]*(n+1)
b_acum = [0]*(m+1)

ap = []
bp = []

s = 0
for i in range(n+1):
    s += al[i]
    a_acum[i] = s
for i in range(1, n+1):
    for j in range(i, n+1):
        ap.append(a_acum[j]-a_acum[i-1])

s = 0
for i in range(m+1):
    s += bl[i]
    b_acum[i] = s
for i in range(1, m+1):
    for j in range(i, m+1):
        bp.append(b_acum[j]-b_acum[i-1])

ap.sort()
bp.sort()

ans = 0
for i in range(len(ap)):
    remain = t-ap[i]

    # lower bound
    left = 0
    right = len(bp)
    while left < right:
        mid = (left+right)//2
        if bp[mid] >= remain:
            right = mid
        else:
            left = mid+1
    b1 = right

    # upper bound
    left = 0
    right = len(bp)
    while left < right:
        mid = (left+right)//2
        if bp[mid] > remain:
            right = mid
        else:
            left = mid+1
    b2 = right

    ans += b2-b1

print(ans)
