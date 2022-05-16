from collections import deque
import math
import sys


def ccw(x, y, z):
    a, b = x
    c, d = y
    e, f = z
    v1 = (c-a, d-b)
    v2 = (e-c, f-d)
    m = v1[0]*v2[1]-v1[1]*v2[0]
    if m > 0:
        return 1
    if m < 0:
        return -1
    if m == 0:
        return 0


def dist(a, b):
    return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])


def comp(v):
    return -math.atan2(v[1]-first[1], v[0]-first[0])


def comp2(v):
    return v[1]*100000-v[0]


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    nn = n//5
    if n % 5 != 0:
        nn += 1
    for i in range(nn):
        tmp = [int(x) for x in sys.stdin.readline().strip().split()]
        for j in range(0, len(tmp), 2):
            arr.append((tmp[j], tmp[j+1]))

    arr.sort(key=comp2)
    first = arr[-1]
    rm = arr[:-1]

    rm.sort(key=comp)
    i = 0
    while i < len(rm)-1:
        # print(comp(rm[i]), comp(rm[i+1]), comp(rm[i]) == comp(rm[i+1]))
        if comp(rm[i]) == comp(rm[i+1]):
            if dist(first, rm[i]) > dist(first, rm[i+1]):
                rm.pop(i+1)
            else:
                rm.pop(i)
        else:
            i += 1
    # print(rm)
    q = [first, rm[0]]

    i = 1
    while i < len(rm):
        # print(q)
        c = ccw(q[-2], q[-1], rm[i])
        # print(q[-2], q[-1], rm[i], c)
        if c == -1:
            q.append(rm[i])
            i += 1
        else:
            q.pop()

    print(len(q))
    for i in q:
        print(i[0], i[1])
