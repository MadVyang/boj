from collections import deque


n, m = [int(x) for x in input().split()]
board = [[int(x) for x in input().split()] for _ in range(n)]

empty_count = 0
vpos = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            empty_count += 1
        if board[i][j] == 2:
            vpos.append((i, j))

apos = []


def sim():
    global empty_count
    if empty_count==0:
        return 0
    nq = deque(apos)
    vis = set(apos)
    count = 0
    for k in range(123456789):
        if not nq:
            return 123456789
        q = nq.copy()
        nq.clear()
        while q:
            i, j = q.pop()
            # print(i, j, count, empty_count)
            if board[i][j] == 0:
                count += 1
                if count == empty_count:
                    return k
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < n:
                    if board[ni][nj] in [0, 2] and (ni, nj) not in vis:
                        vis.add((ni, nj))
                        nq.append((ni, nj))
    return 123456789


ans = 123456789


def dfs(i):
    global m, ans
    if len(apos) == m:
        ans = min(ans, sim())
        return
    if i == len(vpos):
        return
    apos.append(vpos[i])
    dfs(i+1)
    apos.pop()
    dfs(i+1)


dfs(0)

if ans == 123456789:
    ans = -1
print(ans)
