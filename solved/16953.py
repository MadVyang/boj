a, b = [int(x) for x in input().split()]


def dfs(current, count):
    global a, b
    if current == b:
        return count
    if current > b:
        return 123456789
    return min(dfs(current * 2, count + 1), dfs(current * 10 + 1, count + 1))


ans = dfs(a, 0) + 1
if ans >= 123456789:
    ans = -1
print(ans)

