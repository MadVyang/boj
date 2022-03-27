t = int(input())
for _ in range(t):
    y = 0
    k = 0
    for i in range(9):
        a, b = [int(x) for x in input().split()]
        y += a
        k++b
    if y > k:
        print('Yonsei')
    elif y < k:
        print('Korea')
    else:
        print('Draw')
