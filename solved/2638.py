import sys
sys.setrecursionlimit(10**6)

n, m = [int(x) for x in input().split()]
board = [[int(x) for x in input().split()] for _ in range(n)]
for line in board:
    line.insert(0, 0)
    line.append(0)
board.insert(0, [0]*(m+2))
board.append([0]*(m+2))
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def print_board():
    for line in board:
        print(' '.join([str(x) for x in line]))


def dfs(i, j, color):
    global n, m
    if i < 0 or j < 0 or i == n+2 or j == m+2:
        return
    if board[i][j] == 1 or board[i][j] == color:
        return
    board[i][j] = color
    for dir in dirs:
        dfs(i+dir[0], j+dir[1], color)


time = 1
while True:
    dfs(0, 0, time+1)
    done = True
    for i in range(n+2):
        for j in range(m+2):
            if board[i][j] == 1:
                count = 0
                for dir in dirs:
                    if board[i+dir[0]][j+dir[1]] == time+1:
                        count += 1
                if count >= 2:
                    board[i][j] = 0
                else:
                    done = False
    if done:
        break
    time += 1
print(time)
