a, b = map(int, input().split())


def sol(x):
    if x == 0:
        return 1
    r = 1
    for i in range(1, x):
        r = r*2+(1 << i)
    return r+1


def solve(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    one_pos = 64
    while one_pos >= 0:
        if n & (1 << one_pos) > 0:
            break
        one_pos -= 1
    r = sol(one_pos)

    cur = n-(1 << one_pos)
    one_pos -= 1
    while one_pos >= 0:
        if n & (1 << one_pos) > 0:
            r += cur+sol(one_pos)
            # print(n, r, cur, sol(one_pos), one_pos)
            cur -= 1 << one_pos
        one_pos -= 1
    return r


def naive(n):
    r = 0
    while n > 0:
        if n & 1 == 1:
            r += 1
        n >>= 1
    return r


def naive_s(a, b):
    r = 0
    for i in range(a, b+1):
        r += naive(i)
    return r


# print(naive_s(a, b))
ans = solve(b)-solve(a-1)
print(ans)
