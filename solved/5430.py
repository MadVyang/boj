t = int(input())
for _ in range(t):
    op = input()
    n = int(input())
    arr = input()
    # print(arr[1:-1])
    if n > 0:
        arr = [int(x) for x in arr[1:-1].split(',')]
    else:
        arr = []

    d = True
    s, e = 0, n
    err = False
    for p in op:
        if p == 'R':
            d = not d
        else:
            if s >= e:
                err = True
                break
            if d:
                s += 1
            else:
                e -= 1
    if err:
        print('error')
    else:
        arr = [str(x) for x in arr[s:e]]
        if not d:
            arr.reverse()
        print('['+','.join(arr)+']')
