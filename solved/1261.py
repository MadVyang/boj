from collections import deque


m, n = map(int, input().split())
board = []
for i in range(n):
    board.append([int(x) for x in input()])

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque([(0, 0, 0)])
vis = {(0, 0): 0}
while q:
    i, j, c = q.popleft()
    if c > vis[(i, j)]:
        continue
    for di, dj in dirs:
        ii, jj = i+di, j+dj
        if 0 <= ii < n and 0 <= jj < m:
            if (ii, jj) not in vis or vis[(ii, jj)] > vis[(i, j)]:
                vis[(ii, jj)] = vis[(i, j)]
                if board[ii][jj] == 1:
                    vis[(ii, jj)] += 1
                    q.append((ii, jj, vis[(ii, jj)]))
                else:
                    q.appendleft((ii, jj, vis[(ii, jj)]))

print(vis[(n-1, m-1)])
