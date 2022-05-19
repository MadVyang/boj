n = int(input())

mem = {}


def solve(n):
    if n in mem:
        return mem[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    m = n//2
    if n % 2 == 0:
        a = solve(m)
        b = solve(m-1)
        mem[n] = (a*(a+2*b)) % 1000000007
        return mem[n]
    a = solve(m)
    b = solve(m+1)
    mem[n] = (a*a+b*b) % 1000000007
    return mem[n]


print(solve(n))
