from collections import deque


n, m = [int(x) for x in input().split()]
arr = [i for i in range(101)]
v = [False for i in range(101)]
for i in range(n+m):
    x, y = [int(x) for x in input().split()]
    arr[x] = y

q = deque()
q.appendleft((1, 0))
v[1] = True

while q:
    i, count = q.pop()
    if i == 100:
        print(count)
        break
    for j in range(1, 7):
        if i+j <= 100 and not v[arr[i+j]]:
            q.appendleft((arr[i+j], count+1))
            v[arr[i+j]] = True
