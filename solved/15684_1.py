import sys


n, m, h = map(int, sys.stdin.readline().strip().split())
ladder = []
for i in range(n+1):
    ladder.append([False]*h)
for i in range(m):
    a, b, = map(int, sys.stdin.readline().strip().split())
    ladder[b][a-1] = True


def sim():
    for i in range(1, n+1):
        cur = i
        for j in range(h):
            if ladder[cur-1][j]:
                cur -= 1
            elif ladder[cur][j]:
                cur += 1
        if cur != i:
            return False
    return True


solved = False


def dfs(max, cur, ii, jj):
    global solved
    if solved:
        return
    if max == cur:
        solved = sim()
        return
    for i in range(ii, n):
        sj = jj+1 if i == ii else 0
        for j in range(sj, h):
            if not ladder[i][j]:
                ladder[i][j] = True
                dfs(max, cur+1, i, j)
                ladder[i][j] = False


ans = -1
for k in range(4):
    solved = False
    dfs(k, 0, 1, -1)
    if solved:
        ans = k
        break
print(ans)
