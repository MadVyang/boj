n = int(input())
arr = [[int(x) for x in input().split()] for i in range(n)]


def dfs(i, j, size):
    if size == 1:
        if arr[i][j] == 0:
            return (1, 0)
        return (0, 1)
    white = 0
    blue = 0
    for y in range(i, i+size):
        for x in range(j, j+size):
            if arr[y][x] == 0:
                white += 1
            else:
                blue += 1
            if white > 0 and blue > 0:
                s = size//2
                w1, b1 = dfs(i, j, s)
                w2, b2 = dfs(i+s, j, s)
                w3, b3 = dfs(i, j+s, s)
                w4, b4 = dfs(i+s, j+s, s)
                return (w1+w2+w3+w4, b1+b2+b3+b4)
    if white > 0:
        return (1, 0)
    return (0, 1)


w, b = dfs(0, 0, n)
print(w)
print(b)
