from dis import dis
from queue import Queue

n = int(input())
friend = [[False]*(n+1) for _ in range(n+1)]
while True:
    a, b = [int(x) for x in input().split()]
    if a == -1:
        break
    friend[a][b] = True
    friend[b][a] = True

min_score = 9999999
scores = [0]*(n+1)
for i in range(1, n+1):
    q = Queue()
    visited = [False]*(n+1)
    q.put((i, 0))
    score = -1
    while not q.empty():
        cur, dist = q.get()
        visited[cur] = True
        # print(i, cur, dist)
        if dist > score:
            score = dist
        for j in range(1, n+1):
            if friend[cur][j] and not visited[j]:
                visited[j] = True
                q.put((j, dist+1))
    scores[i] = score
    if min_score > score:
        min_score = score

cands = [str(x) for x in range(1, n+1) if scores[x] == min_score]
print(min_score, len(cands))
print(' '.join(cands))
