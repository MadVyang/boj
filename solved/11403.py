from collections import deque


n = int(input())
arr = [[int(x) for x in input().split()] for i in range(n)]

d = [{x: False for x in range(n)} for i in range(n)]

q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            q.append((i, j))
            d[i][j] = True

while q:
    i, j = q.pop()
    for k in range(n):
        if not d[i][k] and d[j][k] == True:
            q.append((i, k))
            d[i][k] = True

for i in range(n):
    s = ''
    for j in range(n):
        if d[i][j]:
            s += '1'
        else:
            s += '0'
        s += ' '
    print(s)
