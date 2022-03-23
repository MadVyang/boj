n = int(input())
r = [0]*10


def count(n, i):
    while n > 0:
        r[n % 10] += 10**i
        n //= 10


def solve(a, b, i):
    while a % 10 != 0 and a < b:
        count(a, i)
        a += 1
    while b % 10 != 9 and b > a:
        count(b, i)
        b -= 1
    if a == b:
        count(a, i)
        return
    for j in range(10):
        r[j] += (b//10-a//10+1)*10**i
    solve(a//10, b//10, i+1)


solve(1, n, 0)

print(' '.join([str(x) for x in r]))
