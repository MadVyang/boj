import sys


n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip().split()])


m, z, p = (0, 0, 0)


def dfs(y, x, size):
    global m, z, p
    d = {0: 0, 1: 0, -1: 0}
    for i in range(y, y+size):
        for j in range(x, x+size):
            d[arr[i][j]] += 1
            if d[0] * d[1] > 0 or d[0] * d[-1] > 0 or d[-1] * d[1] > 0:
                ns = size//3
                dfs(y, x, ns)
                dfs(y, x+ns, ns)
                dfs(y, x+ns*2, ns)
                dfs(y+ns, x, ns)
                dfs(y+ns, x+ns, ns)
                dfs(y+ns, x+ns*2, ns)
                dfs(y+ns*2, x, ns)
                dfs(y+ns*2, x+ns, ns)
                dfs(y+ns*2, x+ns*2, ns)
                return
    # print(d, m, z, p)
    if d[-1] > 0:
        m += 1
        return
    elif d[1] > 0:
        p += 1
        return
    elif d[0] > 0:
        z += 1
        return
    else:
        print('뭐야 시발')


dfs(0, 0, n)

print(m)
print(z)
print(p)
