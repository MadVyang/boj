from collections import deque


n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])
white = deque()
black = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            if (i+j) % 2 == 0:
                white.append((i, j))
            else:
                black.append((i, j))


def fill(y, x, dy, dx):
    s = set()
    _y, _x = y+dy, x+dx
    while 0 <= _y < n and 0 <= _x < n:
        if arr[_y][_x] == 1:
            s.add((_y, _x))
            arr[_y][_x] = 2
        _y += dy
        _x += dx
    return s


def solve(count, emp):
    global n
    r = 0
    if emp:
        y, x = emp.pop()
        r = max(r, solve(count, emp))

        if arr[y][x] == 1:
            s = set([(y, x)])
            arr[y][x] = 3
            s.update(fill(y, x, 1, 1))
            s.update(fill(y, x, -1, 1))
            s.update(fill(y, x, 1, -1))
            s.update(fill(y, x, -1, -1))
            # print(emp)

            tmp = deque()
            if emp:
                ny, nx = emp.pop()
                tmp.append((ny, nx))
                while emp and arr[ny][nx] > 1:
                    ny, nx = emp.pop()
                    tmp.append((ny, nx))
                if arr[ny][nx] == 1:
                    emp.append(tmp.pop())

            r = max(r, solve(count+1, emp))
            while tmp:
                emp.append(tmp.pop())
            for _y, _x in s:
                arr[_y][_x] = 1

        emp.append((y, x))
        return r

    else:
        # a = 0
        # for i in range(n):
        #     for j in range(n):
        #         if arr[i][j] == 3:
        #             a += 1
        return count


w, b = 0, 0
if white:
    w = solve(0, white)
if black:
    b = solve(0, black)

print(w+b)
