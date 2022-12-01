n, s = map(int, input().split())
arr = [int(x) for x in input().split()]
first_half = {}
second_half = {}
half = n//2
ans = 0
cur = 0


def dfs(i, b):
    global cur, half, ans
    if i == half:
        if not b:
            return
        if cur == s:
            ans += 1
        if cur not in first_half:
            first_half[cur] = 0
        first_half[cur] += 1
        return
    cur += arr[i]
    dfs(i+1, True)
    cur -= arr[i]
    dfs(i+1, b)


cur = 0
dfs(0, False)


def dfs2(i, b):
    global cur, n, ans
    if i == n:
        if not b:
            return
        if cur == s:
            ans += 1
        if cur not in second_half:
            second_half[cur] = 0
        second_half[cur] += 1
        return
    cur += arr[i]
    dfs2(i+1, True)
    cur -= arr[i]
    dfs2(i+1, b)


# if n % 2 == 1:
#     half += 1
cur = 0
dfs2(half, False)

# print(first_half, second_half)

for i in first_half:
    if s-i in second_half:
        ans += first_half[i]*second_half[s-i]

print(ans)
