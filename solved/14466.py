import sys


def input():
    return sys.stdin.readline().strip()


n, k, r = [int(x) for x in input().split()]

board = [[0]*(n+1) for _ in range(n+1)]  # 0: 아직 색칠 x
rwall = [[False]*(n+2) for _ in range(n+2)]  # 블럭 상단
cwall = [[False]*(n+2) for _ in range(n+2)]  # 블럭 좌측
for i in range(r):
    r1, c1, r2, c2 = [int(x) for x in input().split()]
    if r1 > r2:
        rwall[r1][c1] = True
    elif r2 > r1:
        rwall[r2][c2] = True
    elif c1 > c2:
        cwall[r1][c1] = True
    elif c2 > c1:
        cwall[r2][c2] = True


cows = [[int(x) for x in input().split()] for _ in range(k)]


def dfs(i, j, color):
    global n
    if i < 1 or j < 1 or i > n or j > n:
        return
    if board[i][j] > 0:
        return
    board[i][j] = color

    if not rwall[i][j]:
        dfs(i-1, j, color)
    if not rwall[i+1][j]:
        dfs(i+1, j, color)
    if not cwall[i][j]:
        dfs(i, j-1, color)
    if not cwall[i][j+1]:
        dfs(i, j+1, color)


color = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == 0:
            dfs(i, j, color)
            color += 1

cow_count = [0]*color
for cow in cows:
    cow_count[board[cow[0]][cow[1]]] += 1

ans = 0
for i in range(1, color):
    for j in range(i+1, color):
        ans += cow_count[i]*cow_count[j]

print(ans)
