from collections import deque


n = int(input())
m = int(input())
if m == 0:
    ans = len(str(n))
    ans = min(ans, abs(n-100))
    print(ans)
    exit()
btn = set([i for i in range(10)]) - set([int(x) for x in input().split()])
q = deque([(100, 0, False)])
vis = set([])
vvis = set([])
while q:
    cur, count, check = q.popleft()
    if cur == n:
        print(count)
        break

    for i in btn:
        if i not in vis:
            vis.add(i)
            q.append((i, count+1, True))
        if check and cur*10+i <= n*3 and cur*10+i not in vvis:
            vvis.add(cur*10+i)
            q.append((cur*10+i, count+1, True))

    if cur+1 not in vis:
        vis.add(cur+1)
        q.append((cur+1, count+1, False))
    if cur > 0 and cur-1 not in vis:
        vis.add(cur-1)
        q.append((cur-1, count+1, False))
