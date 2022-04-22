from collections import deque


n, m = [int(x) for x in input().split()]
arr = [[int(x) for x in input()] for i in range(n)]
vis = [[False]*m for i in range(n)]

q = deque([(0, 0, 1)])
while q:
    i, j, count = q.popleft()
    if i == n-1 and j == m-1:
        print(count)
        break
    vis[i][j] = True
    if i > 0 and arr[i-1][j] == 1 and not vis[i-1][j]:
        q.append((i-1, j, count+1))
    if j > 0 and arr[i][j-1] == 1 and not vis[i][j-1]:
        q.append((i, j-1, count+1))
    if i < n-1 and arr[i+1][j] == 1 and not vis[i+1][j]:
        q.append((i+1, j, count+1))
    if j < m-1 and arr[i][j+1] == 1 and not vis[i][j+1]:
        q.append((i, j+1, count+1))
