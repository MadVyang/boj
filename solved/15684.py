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


mn = math.inf


def dfs(row, count):
    global mn
    if check():
        mn = min(count, mn)
    if count == 3:
        return
    for i in range(row, h+1):
        for j in range(1, n):
            if ladder[i][j]:
                continue
            if not ladder[i][j-1] and not ladder[i][j+1]:
                ladder[i][j] = True
                dfs(i, count+1)
                ladder[i][j] = False


dfs(1, 0)
if mn == math.inf:
    mn = -1
print(mn)
