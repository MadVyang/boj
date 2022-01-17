def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort(reverse=True)
    # print(arr)
    if n == 1:
        print('INFINITY')
        continue
    k = arr[0]-arr[1]
    ans = k
    for i in range(1, n-1):
        d = arr[i]-arr[i+1]
        ans = gcd(k, d)
        k = ans
    if ans == 0:
        print('INFINITY')
        continue
    # if ans < 0:
    #     print(-ans)
    print(ans)
