from collections import deque


n = int(input())
board = []
cost = []
for i in range(n):
    board.append([int(x) for x in input()])
    cost.append([0]*n)

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque([(0, 0)])
vis = {(0, 0): 0}
while q:
    i, j = q.popleft()
    for di, dj in dirs:
        ii, jj = i+di, j+dj
        if 0 <= ii < n and 0 <= jj < n:
            if (ii, jj) not in vis or vis[(ii, jj)] > vis[(i, j)]:
                vis[(ii, jj)] = vis[(i, j)]
                if board[ii][jj] == 0:
                    vis[(ii, jj)] += 1
                q.append((ii, jj))

print(vis[(n-1,n-1)])
