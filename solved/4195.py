import sys


t = int(input())
for _ in range(t):
    f = int(sys.stdin.readline().strip())
    d = {}
    for _ in range(f):
        a, b = sys.stdin.readline().strip().split()
        if not a in d and not b in d:
            ns = set([a, b])
            d[a] = ns
            d[b] = ns
        elif a in d and not b in d:
            d[a].add(b)
            d[b] = d[a]
        elif not a in d and b in d:
            d[b].add(a)
            d[a] = d[b]
        elif d[a] is not d[b]:
            d[a].update(d[b])
            for c in d[b]:
                d[c] = d[a]
        # print(a, b, d[a], d[b], id(d[a]), id(d[b]))
        print(len(d[a]))
