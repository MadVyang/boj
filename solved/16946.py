from collections import deque
import sys


n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip()])

ones = {}
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ones[(i, j)] = True
            pass

st = deque()
count = {}
vis = {}
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

color = 2
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            vis[(i, j)] = True
            arr[i][j] = color
            if color not in count:
                count[color] = 0
            count[color] += 1
            st.append((i, j, color))
            color += 1
            while st:
                y, x, c = st.pop()
                for dy, dx in dirs:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < n and 0 <= nx < m:
                        if arr[ny][nx] == 0 and (ny, nx) not in vis:
                            vis[(ny, nx)] = True
                            arr[ny][nx] = c
                            if c not in count:
                                count[c] = 0
                            count[c] += 1
                            st.append((ny, nx, c))

# print(arr)
# print(count)

# print(count)
# for i in range(n):
#     print(''.join([str(x % 10) for x in arr[i]]))

for y, x in ones:
    tmp = {}
    for dy, dx in dirs:
        ny, nx = y+dy, x+dx
        if (ny, nx) not in ones and 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] not in tmp:
                arr[y][x] += count[arr[ny][nx]]
                tmp[arr[ny][nx]] = True


for i in range(n):
    for j in range(m):
        if (i, j) in ones:
            arr[i][j] -= 0
        else:
            arr[i][j] = 0

for i in range(n):
    print(''.join([str(x % 10) for x in arr[i]]))
