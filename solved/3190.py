n = int(input())
k = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
snake = [(1, 1)]
for _ in range(k):
    y, x = [int(x) for x in input().split()]
    arr[y][x] = 1
l = int(input())
com = ['']*10005
for _ in range(l):
    x, w = [x for x in input().split()]
    x = int(x)
    com[x] = w

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
d = 0
end = -1
for i in range(1, 20000):
    _y = snake[0][0]
    _x = snake[0][1]
    snake.append(snake[len(snake)-1])
    for s in range(len(snake)-2, 0, -1):
        snake[s] = snake[s-1]
    snake[0] = (_y+dirs[d][0], _x+dirs[d][1])
    y = snake[0][0]
    x = snake[0][1]
    if x < 1 or y < 1 or x > n or y > n:
        end = i
        break
    for s in range(1, len(snake)):
        if snake[0][0] == snake[s][0] and snake[0][1] == snake[s][1]:
            end = i
            break
    if end > 0:
        break
    if arr[y][x] == 1:
        arr[y][x] = 0
    else:
        snake.pop()

    if com[i] == 'D':
        if d == 0:
            d = 2
        elif d == 1:
            d = 3
        elif d == 2:
            d = 1
        else:
            d = 0
    elif com[i] == 'L':
        if d == 0:
            d = 3
        elif d == 1:
            d = 2
        elif d == 2:
            d = 0
        else:
            d = 1

print(end)
