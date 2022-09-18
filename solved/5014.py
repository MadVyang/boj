from collections import deque

f, s, g, u, d = map(int, input().split())
vis = set([s])
q = deque([(s, 0)])
while q:
    i, n = q.popleft()
    if i == g:
        print(n)
    if i+u <= f and i+u not in vis:
        vis.add(i+u)
        q.append((i+u, n+1))
    if i-d >= 0 and i-d not in vis:
        vis.add(i-d)
        q.append((i-d, n+1))

if g not in vis:
    print('use the stairs')
