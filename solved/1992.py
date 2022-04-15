n = int(input())
arr = [[int(x) for x in input()] for i in range(n)]


def dfs(i, j, size):
    if size == 1:
        if arr[i][j] == 0:
            return '0'
        return '1'
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
                ans = '('
                ans += dfs(i, j, s)
                ans += dfs(i, j+s, s)
                ans += dfs(i+s, j, s)
                ans += dfs(i+s, j+s, s)
                ans += ')'
                return ans
    if white > 0:
        return '0'
    return '1'


print(dfs(0, 0, n))
