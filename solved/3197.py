from collections import deque
import sys

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
r, c = map(int, input().split())
board = [[x for x in sys.stdin.readline().strip()] for i in range(r)]
si, sj = -1, 0
ei, ej = 0, 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            if si == -1:
                si, sj = i, j
            else:
                ei, ej = i, j
            board[i][j] = '.'


root = [[(0, 0)]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        root[i][j] = (i, j)


def find(i, j):
    if root[i][j] == (i, j):
        return (i, j)
    root[i][j] = find(root[i][j][0], root[i][j][1])
    return root[i][j]


def union(ai, aj, bi, bj):
    ra = find(ai, aj)
    rb = find(bi, bj)
    if ra > rb:
        root[ra[0]][ra[1]] = rb
    else:
        root[rb[0]][rb[1]] = ra


q = deque()
nq = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == '.':
            check = False
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if not (0 <= ni < r and 0 <= nj < c):
                    continue
                if board[ni][nj] == '.':
                    union(i, j, ni, nj)
                else:
                    check = True
            if check:
                nq.append((i, j))

for k in range(1500):
    if find(si, sj) == find(ei, ej):
        print(k)
        break
    q = nq.copy()
    nq.clear()

    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i+di, j+dj
            if not (0 <= ni < r and 0 <= nj < c):
                continue
            if find(i,j)!=find(ni,nj):
                union(i, j, ni, nj)

            if board[ni][nj] == 'X':
                nq.append((ni, nj))
                board[ni][nj] = '.'
                for ddi, ddj in dirs:
                    nni, nnj = ni+ddi, nj+ddj
                    if not (0 <= nni < r and 0 <= nnj < c):
                        continue
                    if board[nni][nnj] == '.' and find(ni, nj) != find(nni, nnj):
                        union(ni, nj, nni, nnj)
    
