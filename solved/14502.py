n, m = [int(x) for x in input().split()]
arr = []
tmp = []
for i in range(n):
    _arr = [int(x) for x in input().split()]
    arr.append(_arr)


def fill(i, j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return
    # print(tmp)
    if tmp[i][j] == 3:
        return
    if tmp[i][j] == 0:
        tmp[i][j] = 3
        fill(i-1, j)
        fill(i, j-1)
        fill(i+1, j)
        fill(i, j+1)


def check():
    global tmp
    tmp = []
    for i in range(n):
        tmp.append([])
        for j in range(m):
            tmp[i].append(arr[i][j])

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                tmp[i][j] = 0
                fill(i, j)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt


def solve(c, y, x):
    if c == 3:
        return check()
    # if x == m:
    #     return solve(c, y+1, 0)
    # if y == n:
    #     return -1
    mx = 0
    for i in range(0, n):
        for j in range(0, m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                r = solve(c+1, y, x+1)
                if r > mx:
                    mx = r
                arr[i][j] = 0
    return mx


print(solve(0, 0, 0))
