from collections import deque


n, k = [int(x) for x in input().split()]


q = deque([(n, 0)])
vis = [False]*200003
tt = -1
ans = 0

while q:
    i, t = q.popleft()
    if i == k:
        if tt == -1:
            tt = t
        if t == tt:
            ans += 1
        continue
    # if vis[i]:
    #     continue
    vis[i] = True

    if i > 0 and not vis[i-1]:
        q.append((i-1, t+1))
    if i < 100001:
        if not vis[i+1]:
            q.append((i+1, t+1))
        if not vis[i*2]:
            q.append((i*2, t+1))

print(tt)
print(ans)
