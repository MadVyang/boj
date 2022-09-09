import sys


n = int(input())
mx = [0, 0, 0]
mn = [0, 0, 0]
for i in range(n):
    tmp = [int(x) for x in sys.stdin.readline().split()]

    nmx = [0, 0, 0]
    nmx[0] = max(mx[0], mx[1])+tmp[0]
    nmx[1] = max(mx[0], mx[1], mx[2])+tmp[1]
    nmx[2] = max(mx[2], mx[1])+tmp[2]
    mx = nmx[:]

    nmn = [0, 0, 0]
    nmn[0] = min(mn[0], mn[1])+tmp[0]
    nmn[1] = min(mn[0], mn[1], mn[2])+tmp[1]
    nmn[2] = min(mn[2], mn[1])+tmp[2]
    mn = nmn[:]

print(max(mx), min(mn))
