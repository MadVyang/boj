a, b, c = [int(x) for x in input().split()]


def power(a, b):
    global c
    if b == 0:
        return 1
    if b == 1:
        return a%c
    r = 1
    if b % 2 == 1:
        r = a
    t = power(a, b//2)
    return (t*t*r) % c


print(power(a, b))
