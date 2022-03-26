import math


n, m, h = [int(x) for x in input().split()]
ladder = [[False]*(n+2) for _ in range(h+1)]
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    ladder[a][b] = True


def check():
    for i in range(1, n+1):
        current = i
        for j in range(1, h+1):
            if ladder[j][current]:
                current += 1
            elif ladder[j][current-1]:
                current -= 1
        if current != i:
            return False
    return True


def dfs(row, count, mcount):
    if count > 3:
        return math.inf
    if count == mcount:
        if check():
            return count
        return math.inf
    mn = math.inf
    for i in range(row, h+1):
        for j in range(1, n):
            if ladder[i][j]:
                continue
            if not ladder[i][j-1] and not ladder[i][j+1]:
                ladder[i][j] = True
                mn = min(mn, dfs(i, count+1, mcount))
                ladder[i][j] = False
    return mn


ans = math.inf
for i in range(0, 4):
    ans = min(ans, dfs(1, 0, i))
if ans == math.inf:
    ans = -1
print(ans)
