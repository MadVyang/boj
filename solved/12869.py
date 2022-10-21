n = int(input())
arr = [int(x) for x in input().split()]
if n == 1:
    if arr[0] % 9 == 0:
        print(arr[0]//9)
    else:
        print(arr[0]//9+1)
elif n == 2:
    dp = {}
    def solve(a, b):
        if a <= 0 and b <= 0:
            return 0
        if a <= 0:
            if b % 9 == 0:
                return b//9
            else:
                return b//9+1
        if b <= 0:
            if a % 9 == 0:
                return a//9
            else:
                return a//9+1
        if (a, b) in dp:
            return dp[(a, b)]
        dp[(a, b)] = 123456789
        for da, db in [(9, 3), (3, 9)]:
            dp[(a, b)] = min(dp[(a, b)], solve(a-da, b-db)+1)
        return dp[(a, b)]
    ans = solve(arr[0], arr[1])
    # if ans >= 123456789:
    #     ans = 1
    print(ans)
else:
    dp = {}

    def solve(a, b, c):
        if a <= 0 and b <= 0 and c <= 0:
            return 0
        if a <= 0 and b <= 0:
            if c % 9 == 0:
                return c//9
            else:
                return c//9+1
        if c <= 0 and b <= 0:
            if a % 9 == 0:
                return a//9
            else:
                return a//9+1
        if a <= 0 and c <= 0:
            if b % 9 == 0:
                return b//9
            else:
                return b//9+1

        if (a, b,c ) in dp:
            return dp[(a, b,c)]
        dp[(a, b,c)] = 123456789
        for da, db, dc in [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]:
            dp[(a, b, c)] = min(dp[(a, b, c)], solve(a-da, b-db, c-dc)+1)
        return dp[(a, b,c)]
    ans = solve(arr[0], arr[1], arr[2])
    # if ans >= 123456789:
    #     ans = 1
    print(ans)
