n, m = [int(x) for x in input().split()]
arr = []


if n % m == 0:
    print(0)
else:
    n %= m
    n_save = n
    m_save = m
    # print(n_save, m_save)
    gcd = 1
    for i in range(2, n_save+1):
        while n % i == 0 and m % i == 0:
            n = n//i
            m = m//i
            gcd *= i
    print(gcd*(m-1))
