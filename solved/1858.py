import math
import sys


n = int(input())
arr = []
dct = {}
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip().split()])
    dct[(arr[i][0], arr[i][1])] = i
orig = arr[:]
arr.sort(key=lambda x: x[0])

y, x = 0, 1
ax, ay = 0, 0
ai, bi = 123456789, 123456789
for i in range(n-1):
    a, b = arr[i][0], arr[i][1]
    c, d = arr[i+1][0], arr[i+1][1]
    aai, bbi = dct[(a, b)], dct[(c, d)]
    if aai > bbi:
        tmp = aai
        aai = bbi
        bbi = tmp

    yy, xx = abs(b-d), abs(c-a)
    if xx*y < x*yy:
        y, x = yy, xx
        ai, bi = aai, bbi
        ax, ay = orig[ai][0], orig[ai][1]
    elif xx*y == x*yy:
        if ai > aai:
            y, x = yy, xx
            ai, bi = aai, bbi
            ax, ay = orig[ai][0], orig[ai][1]

for i in range(n):
    a, b = arr[i][0], arr[i][1]
    bbi = dct[(a, b)]
    if bbi == ai:
        continue
    yy, xx = abs(ay-b), abs(a-ax)
    if xx*y == x*yy and bi > bbi:
        bi = bbi

print(ai+1, bi+1)
