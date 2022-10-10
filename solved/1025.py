n, m = map(int, input().split())
arr = [[int(x) for x in input()] for _ in range(n)]

sqrs = set()
for i in range(1, 100000):
    sqrs.add(i*i)

cur = 0
ans = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans = 0
            break
        if arr[i][j] in sqrs:
            ans = max(ans, arr[i][j])
            break


def dfs(si, sj, di, dj, k):
    global cur, ans
    i, j = si+di*k, sj+dj*k
    # print(si, sj, di, dj, k, cur)
    if not (di == 0 and dj == 0) and 0 <= i < n and 0 <= j < m:
        cur *= 10
        cur += arr[i][j]
        dfs(si, sj, di, dj, k+1)
        cur //= 10
    if cur in sqrs:
        ans = max(ans, cur)


for si in range(n):
    for sj in range(m):
        for di in range(-n+1, n):
            for dj in range(-m+1, m):
                cur = 0
                dfs(si, sj, di, dj, 0)

print(ans)
