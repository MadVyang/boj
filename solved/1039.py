n, k = [int(x) for x in input().split()]
arr = []
checks = [False]*10
check = False
# print(n, k)

zeros = 0
nonzeros = 0
while n > 0:
    if checks[n % 10] == True:
        check = True
        # print(check)
    else:
        checks[n % 10] = True
    if n % 10 == 0:
        zeros += 1
    arr.append(n % 10)
    n //= 10

arr.reverse()
l = len(arr)


def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def to_num():
    r = 0
    for i in range(l):
        r *= 10
        r += arr[i]
    return r


def solve(c):
    if c == k:
        # print(to_num())
        return to_num()
    if c >= l-2:
        mx = to_num()
        if not check and (k-c) % 2 == 1:
            _mx = -1
            for i in range(0, l):
                for j in range(i+1, l):
                    if i == 0 and arr[j] == 0:
                        continue
                    swap(i, j)
                    r = solve(c+1)
                    if r > _mx:
                        _mx = r
                    swap(i, j)
            mx = _mx
        return mx

    mx = -1
    for i in range(c, l):
        for j in range(i+1, l):
            if i == 0 and arr[j] == 0:
                continue
            swap(i, j)
            r = solve(c+1)
            if r > mx:
                mx = r
            swap(i, j)
    return mx


if l == 1 or (l == 2 and zeros == 1):
    print(-1)
else:
    print(solve(0))
