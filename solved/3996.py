n, k = [int(x) for x in input().split()]
ans = 0


def convert(_n, _k):
    arr = []
    while _n > 0:
        arr.append(_n % _k)
        _n //= _k
    arr.append(0)
    return arr


def convert_convert(arr=[]):
    result = []
    zero_flag = -1
    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(arr[i])
        elif arr[i] > 0:
            arr[i+1] += 1
            zero_flag = len(result)
    for i in range(zero_flag):
        result[i] = 0

    if zero_flag == -1:
        global ans
        ans = 1
    return result


arr = convert(n, k)
conv = convert_convert(arr)
# print(arr)
# print(convert_convert(arr))

r = 1
for i in conv:
    ans += r*i
    r *= k
if n < k:
    print(n+1)
else:
    print(ans)
