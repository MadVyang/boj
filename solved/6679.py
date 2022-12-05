for i in range(1000, 10000):
    oi = i
    s = set()
    for j in [10, 12, 16]:
        i = oi
        a = 0
        for k in range(4):
            # print(oi, i % j)
            a += i % j
            i //= j
        s.add(a)
    if len(s) == 1:
        print(oi)
