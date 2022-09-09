n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])


h = []
c = []

r = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            c.append((i, j))
            r += 1
        if arr[i][j] == 1:
            h.append((i, j))


def check():
    r = 0
    for i, j in h:
        mn = 123456789
        for ii, jj in c:
            if arr[ii][jj] == 2:
                mn = min(mn, abs(i-ii)+abs(j-jj))
        r += mn
    return r


def solve(i, count):
    global m, r
    if count == r-m:
        return check()
    if i == len(c):
        return 1234596789
    y, x = c[i]
    arr[y][x] = 0
    a = solve(i+1, count+1)
    arr[y][x] = 2
    a = min(a, solve(i+1, count))
    return a


print(solve(0, 0))
