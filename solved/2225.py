n, k = map(int, input().split())

mem = []
for i in range(201):
    mem.append([-1]*201)


def dfs(cur, count):
    # print(cur, count)
    if mem[cur][count] != -1:
        return mem[cur][count]
    if count == k:
        if cur == n:
            return 1
        else:
            return 0
    mem[cur][count] = 0
    for i in range(n+1):
        if cur+i <= n:
            mem[cur][count] += dfs(cur+i, count+1)
    mem[cur][count]%=1000000000
    return mem[cur][count]


print(dfs(0, 0))
