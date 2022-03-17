n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def move(board, dir):
    new_board = [board[i][:] for i in range(n)]
    merge_check = [[False]*n for i in range(n)]
    dy, dx = dir
    if dx == 0:
        if dy == 1:
            for j in range(n):
                for i in range(n-2, -1, -1):
                    if new_board[i][j] > 0:
                        merged = False
                        k = i+1
                        while k < n:
                            if new_board[k][j] == 0:
                                new_board[k][j] = new_board[k-1][j]
                                new_board[k-1][j] = 0
                            elif not merged and not merge_check[k][j] and new_board[k-1][j] == new_board[k][j]:
                                new_board[k][j] = new_board[k-1][j]*2
                                new_board[k-1][j] = 0
                                merged = True
                            else:
                                break
                            k += 1
                        k -= 1
                        if merged:
                            merge_check[k][j] = True
        else:
            for j in range(n):
                for i in range(1, n, 1):
                    if new_board[i][j] > 0:
                        merged = False
                        k = i-1
                        while k >= 0:
                            if new_board[k][j] == 0:
                                new_board[k][j] = new_board[k+1][j]
                                new_board[k+1][j] = 0
                            elif not merged and not merge_check[k][j] and new_board[k+1][j] == new_board[k][j]:
                                new_board[k][j] = new_board[k+1][j]*2
                                new_board[k+1][j] = 0
                                merged = True
                            else:
                                break
                            k -= 1
                        k += 1
                        if merged:
                            merge_check[k][j] = True

    else:
        if dx == 1:
            for i in range(n):
                for j in range(n-2, -1, -1):
                    if new_board[i][j] > 0:
                        merged = False
                        k = j+1
                        while k < n:
                            if new_board[i][k] == 0:
                                new_board[i][k] = new_board[i][k-1]
                                new_board[i][k-1] = 0
                            elif not merged and not merge_check[i][k] and new_board[i][k-1] == new_board[i][k]:
                                new_board[i][k] = new_board[i][k-1]*2
                                new_board[i][k-1] = 0
                                merged = True
                            else:
                                break
                            k += 1
                        k -= 1
                        if merged:
                            merge_check[i][k] = True
        else:
            for i in range(n):
                for j in range(1, n, 1):
                    if new_board[i][j] > 0:
                        merged = False
                        k = j-1
                        while k >= 0:
                            if new_board[i][k] == 0:
                                new_board[i][k] = new_board[i][k+1]
                                new_board[i][k+1] = 0
                            elif not merged and not merge_check[i][k] and new_board[i][k+1] == new_board[i][k]:
                                new_board[i][k] = new_board[i][k+1]*2
                                new_board[i][k+1] = 0
                                merged = True
                            else:
                                break
                            k -= 1
                        k += 1
                        if merged:
                            merge_check[i][k] = True
    return new_board


def get_max(board):
    r = 0
    for i in range(n):
        for j in range(n):
            r = max(r, board[i][j])
    return r


def dfs(board, move_count):
    if move_count == 5:
        return get_max(board)
    r = 0
    for dir in dirs:
        r = max(r, dfs(move(board, dir), move_count+1))
    return r


print(dfs(board, 0))


def print_board(board):
    for l in board:
        print(' '.join([str(x) for x in l]))


# print_board(move(board, dirs[0]))
# print_board(move(board, dirs[1]))
# print_board(move(board, dirs[2]))
# print_board(move(board, dirs[3]))
