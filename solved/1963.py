from collections import deque
from math import sqrt


t = int(input())

primes = []
for i in range(4):
    primes.append([[] for _ in range(1000)])
for i in range(1000, 9999):
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            break
    else:
        primes[0][i % 1000].append(i)
        primes[1][(i//1000)*100 + i % 100].append(i)
        primes[2][(i//100)*10 + i % 10].append(i)
        primes[3][i//10].append(i)

for i in range(t):
    a, b = map(int, input().split())

    vis = [False]*10000
    vis[a] = True

    q = deque([(a, 0)])
    while q:
        cur, count = q.popleft()
        if cur == b:
            print(count)
            break

        next_primes = primes[0][cur % 1000]+primes[1][(
            cur//1000)*100 + cur % 100]+primes[2][(cur//100)*10 + cur % 10]+primes[3][cur//10]
        for next in next_primes:
            if not vis[next]:
                q.append((next, count+1))
                vis[next] = True
    else:
        print('Impossible')
