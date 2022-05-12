import sys


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    ga = {}
    gb = {}
    for i in range(n):
        arr.append([int(x) for x in sys.stdin.readline().strip().split()])
        ga[arr[i][0]] = i
        gb[arr[i][1]] = i

    mn = 123456789
    count = 0
    for i in range(1, n+1):
        a = i
        cur = ga[i]
        b = arr[cur][1]
        if b < mn:
            count += 1
            mn = min(mn, b)
    print(count)
