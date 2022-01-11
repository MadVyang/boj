n = int(input())
while n != -1:
    b = 0
    m = 0
    for i in range(n):
        s, t = [int(x) for x in input().split()]
        m += (t-b)*s
        b = t
    print(m, 'miles')
    n = int(input())
