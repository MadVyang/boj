from collections import deque


m, n = map(int, input().split())
board = [input() for i in range(n)]
y, x = 0, 0
ey, ex = 0, 0

xpos = set()
xcount = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            y, x = i, j
        if board[i][j] == 'X':
            xpos.add((i, j))
            xcount += 1
        if board[i][j] == 'E':
            ey, ex = i, j

ans = 0


def solve(ans):
    global y, x
    q = deque([(y, x, 0)])
    vis = [[False]*m for i in range(n)]
    min_dist = 123456789
    r = 123456789
    while q:
        i, j, d = q.popleft()
        if not xpos and board[i][j] == 'E':
            return ans+d
        # if d > min_dist:
        #     continue
        if board[i][j] == 'X' and (i, j) in xpos:
            ty, tx = y, x
            y, x = i, j
            if d < min_dist:
                min_dist = d
            xpos.remove((i, j))
            r = min(r, solve(ans+d))
            xpos.add((i, j))
            y, x = ty, tx
            continue
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and not vis[ni][nj] and board[ni][nj] != '#':
                q.append((ni, nj, d+1))
                vis[ni][nj] = True
    return r


print(solve(0))
