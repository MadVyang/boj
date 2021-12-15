n = int(input())


def solve(k, start, end, middle):
    if (k == 0):
        return
    solve(k - 1, start, middle, end)
    print(start, end)
    solve(k - 1, middle, end, start)


print(2**n-1)
if(n <= 20):
    solve(n, 1, 3, 2)
