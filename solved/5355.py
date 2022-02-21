t = int(input())
for _ in range(t):
    arr = [x for x in input().split()]
    n = float(arr[0])
    for i in arr[1:]:
        if i == '@':
            n *= 3
        if i == '%':
            n += 5
        if i == '#':
            n -= 7
    print('{:.2f}'.format(n))
