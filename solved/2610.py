import heapq


n = int(input())
m = int(input())
g = {}

root = [i for i in range(n+1)]


def find(a):
    if root[a] == a:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        root[a] = b
    else:
        root[b] = a


for i in range(m):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = set()
    if b not in g:
        g[b] = set()
    g[a].add(b)
    g[b].add(a)

    union(a, b)

sets = {}
for i in range(1, n+1):
    if find(i) not in sets:
        sets[find(i)] = set()
    sets[find(i)].add(i)
    if i not in g:
        g[i] = set()
ans = []
for s in sets:
    min_i = list(sets[s])[0]
    min_v = 123456789
    for i in sets[s]:
        d = {}
        q = [(0, i)]
        d[i] = 0
        while q:
            dis, cur = heapq.heappop(q)
            if cur in d and d[cur] < dis:
                continue
            for j in g[cur]:
                if j not in d or d[j] > dis+1:
                    d[j] = dis+1
                    heapq.heappush(q, (dis+1, j))
        if max(d.values()) < min_v:
            min_v = max(d.values())
            min_i = i
        # print(s, i, sum(d.values()))
    ans.append(min_i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)
