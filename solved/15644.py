from queue import Queue

n, m = [int(x) for x in input().split()]
pan = [[x for x in input()] for i in range(n)]

init_red = (0, 0)
init_blue = (0, 0)
goal = (0, 0)
for i in range(n):
    for j in range(m):
        if pan[i][j] == 'B':
            init_blue = (i, j)
        if pan[i][j] == 'R':
            init_red = (i, j)
        if pan[i][j] == 'O':
            goal = (i, j)

        if pan[i][j] != '#':
            pan[i][j] = '.'

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_to_str = {(0, 1):'R', (0, -1):'L', (1, 0):'D', (-1, 0):'U'}

que = Queue()
que.put((init_red, init_blue, 0, ''))

visited = {}

solved = False
while not que.empty():
    red, blue, count, log = que.get()
    # print(red, blue, count)

    if red == goal:
        print(count)
        print(log)
        solved = True
        break

    old_red = red
    old_blue = blue

    for dy, dx in dirs:
        ry, rx = red
        by, bx = blue

        rbreaked = False
        while pan[ry+dy][rx+dx] == '.':
            if (ry+dy, rx+dx) == (by, bx):
                rbreaked = True
                break
            ry += dy
            rx += dx
            if (ry, rx) == goal:
                break
        while pan[by+dy][bx+dx] == '.':
            if (by+dy, bx+dx) == (ry, rx) and (ry, rx) != goal:
                break
            by += dy
            bx += dx
            if (by, bx) == goal:
                break
        if rbreaked:
            while pan[ry+dy][rx+dx] == '.':
                if (ry+dy, rx+dx) == (by, bx):
                    break
                ry += dy
                rx += dx
                if (ry, rx) == goal:
                    break

        new_red = (ry, rx)
        new_blue = (by, bx)

        if new_blue == goal:
            continue

        if new_red == old_red and new_blue == old_blue:
            continue

        if visited.get((new_red, new_blue)) == None and count < 10:
            visited.update({(new_red, new_blue): True})
            que.put((new_red, new_blue, count+1, log+dir_to_str[(dy, dx)]))

if not solved:
    print(-1)
