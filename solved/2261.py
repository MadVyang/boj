import math
import sys


n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip().split()])
arr.sort(key=lambda x: x[0])


def solve(s, e):
    if e-s == 0:
        return math.inf
    if e-s == 1:
        a, b = arr[e]
        c, d = arr[s]
        return (a-c)*(a-c)+(b-d)*(b-d)

    m = (s+e)//2
    mn = solve(s, m)
    mn = min(mn, solve(m+1, e))

    arr2 = []
    for i in range(m, s-1, -1):
        a, b = arr[m+1]
        c, d = arr[i]
        if (c-a)*(c-a) >= mn:
            break
        else:
            arr2.append(arr[i])
    for i in range(m+1, e+1, 1):
        a, b = arr[m]
        c, d = arr[i]
        if (c-a)*(c-a) >= mn:
            break
        else:
            arr2.append(arr[i])

    arr2.sort(key=lambda x: x[1])
    for i in range(len(arr2)):
        for j in range(i+1, len(arr2)):
            a, b = arr2[i]
            c, d = arr2[j]
            if (b-d)*(b-d) >= mn:
                break
            mn = min(mn, (a-c)*(a-c)+(b-d)*(b-d))
    return mn


print(solve(0, n-1))
