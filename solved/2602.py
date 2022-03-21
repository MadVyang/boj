s = input()
a = input()
b = input()

dp = [[[0, 0] for _ in range(len(a))] for _ in range(len(s))]
v = [[[False, False] for _ in range(len(a))] for _ in range(len(s))]


def dfs(si, i, is_a):
    if si == len(s):
        return 1
    if i == len(a):
        return 0
    if v[si][i][is_a]:
        return dp[si][i][is_a]
    v[si][i][is_a] = True

    r = 0
    for j in range(i, len(a)):
        if is_a == 1:
            if a[j] == s[si]:
                r += dfs(si+1, j+1, 1 - is_a)
        else:
            if b[j] == s[si]:
                r += dfs(si+1, j+1, 1 - is_a)
    dp[si][i][is_a] = r
    return r


print(dfs(0, 0, 1)+dfs(0, 0, 0))
