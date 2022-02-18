while True:
    a, b = [int(x) for x in input().split()]
    if a == b and b == 0:
        break
    if a > b:
        print('Yes')
    else:
        print('No')
