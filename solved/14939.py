import math


arr = []
for i in range(10):
    arr.append(list(input()))


def flip(i, j):
    lights = [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for y, x in lights:
        if 0 <= y < 10 and 0 <= x < 10:
            arr[y][x] = '#' if arr[y][x] == 'O' else 'O'


def solve(n):
    # print(arr[0], n)
    ans = n
    flipped = []
    for i in range(1, 10):
        for j in range(10):
            if arr[i-1][j] == 'O':
                flip(i, j)
                flipped.append((i, j))
                ans += 1
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 'O':
                ans = math.inf
    for i, j in flipped:
        flip(i, j)
    return ans


ans = math.inf


def gen(i, n):
    global ans
    if i == 10:
        ans = min(ans, solve(n))
        return
    gen(i+1, n)
    flip(0, i)
    gen(i+1, n+1)
    flip(0, i)


gen(0, 0)
if ans == math.inf:
    ans = -1
print(ans)
