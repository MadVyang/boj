n, b = [int(x) for x in input().split()]
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])


def cal(a, b):
    r = []
    for i in range(n):
        r.append([])
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += a[i][k]*b[k][j]
                tmp %= 1000
            r[i].append(tmp)
    return r


def solve(a, i):
    if i == 1:
        return a
    if i == 2:
        return cal(a, a)
    half = solve(a, i//2)
    if i % 2 == 0:
        return cal(half, half)
    else:
        return cal(cal(half, half), a)


r = solve(arr, b)
for i in range(n):
    s = ''
    for j in range(n):
        s += str(r[i][j] % 1000)+' '
    print(s)
