n, m = map(int, input().split())


def ten(k):
    t, f = 0, 0
    i = 2
    while i <= k:
        t += k//i
        i *= 2
    i = 5
    while i <= k:
        f += k//i
        i *= 5
    return (t, f)


t, f = ten(n)
tt, ff = ten(m)
ttt, fff = ten(n-m)

print(min(t-tt-ttt, f-ff-fff))
