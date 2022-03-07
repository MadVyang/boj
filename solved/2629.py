n = int(input())
chs = [int(x) for x in input().split()]
m = int(input())
gss = [int(x) for x in input().split()]

mem = [[123456789]*120000 for _ in range(n)]


def solve(i, diff):
    if i == n:
        return diff
    if mem[i][diff+60000] != 123456789:
        return mem[i][diff+60000]
    left = solve(i+1, diff+chs[i])
    right = solve(i+1, diff-chs[i])
    notuse = solve(i+1, diff)
    if abs(left) <= abs(right) and abs(left) <= abs(notuse):
        mem[i][diff+60000] = left
    elif abs(right) <= abs(left) and abs(right) <= abs(notuse):
        mem[i][diff+60000] = right
    else:
        mem[i][diff+60000] = notuse
    return mem[i][diff+60000]


ans = ''
for gs in gss:
    a = 'N '
    if solve(0, gs) == 0:
        a = 'Y '
    ans += a
print(ans)
