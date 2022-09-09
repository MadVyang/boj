from collections import deque


r, c = map(int, input().split())
arr = []
for i in range(r):
    arr.append([])
    for j in input():
        arr[i].append(ord(j)-ord('A'))
    # print(arr[i])

q = deque([(0, 0, 1, 1 << arr[0][0])])
vis = {}
ans = 0
while q:
    y, x, count, b = q.popleft()
    if (y, x, b) in vis:
        continue
    vis[(y, x, b)] = 1
    ans = max(ans, count)
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < r and 0 <= nx < c:
            if (b & (1 << arr[ny][nx])) == 0:
                q.append((ny, nx, count+1, b | (1 << arr[ny][nx])))

print(ans)
