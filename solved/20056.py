import sys


n, mm, k = map(int, sys.stdin.readline().strip().split())
balls = []
for i in range(mm):
    r, c, m, s, d = map(int, sys.stdin.readline().strip().split())
    balls.append((r-1, c-1, m, s, d))

for _ in range(k):
    board = {}

    for r, c, m, s, d in balls:
        if d == 0:
            r -= s
            while r < 0:
                r += n
        elif d == 1:
            r -= s
            while r < 0:
                r += n
            c += s
            while c >= n:
                c -= n
        elif d == 2:
            c += s
            while c >= n:
                c -= n
        elif d == 3:
            r += s
            while r >= n:
                r -= n
            c += s
            while c >= n:
                c -= n
        elif d == 4:
            r += s
            while r >= n:
                r -= n
        elif d == 5:
            r += s
            while r >= n:
                r -= n
            c -= s
            while c < 0:
                c += n
        elif d == 6:
            c -= s
            while c < 0:
                c += n
        else:
            r -= s
            while r < 0:
                r += n
            c -= s
            while c < 0:
                c += n
        # if c < 0:
        #     print("???", r, c, m, s, d)
        if (r, c) not in board:
            board[(r, c)] = []
        board[(r, c)].append((r, c, m, s, d))

    balls = []
    for pos in board:
        if len(board[pos]) == 1:
            balls.append(board[pos][0])
        else:
            msum = 0
            ssum = 0
            even = False
            odd = False
            for _, _, m, s, d in board[pos]:
                msum += m
                ssum += s
                if d in [0, 2, 4, 6]:
                    even = True
                else:
                    odd = True

            if msum//5 == 0:
                continue
            if even and odd:
                for dir in [1, 3, 5, 7]:
                    balls.append((pos[0], pos[1], msum//5, ssum//len(board[pos]), dir))
            else:
                for dir in [0, 2, 4, 6]:
                    balls.append((pos[0], pos[1], msum//5, ssum//len(board[pos]), dir))

    # print(balls)
ans = 0
for r, c, m, s, d in balls:
    ans += m
print(ans)
