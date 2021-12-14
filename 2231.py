N = int(input())

def cal(n):
    r = n
    while n>0:
        r += n%10
        n //= 10
    return r

def sol():
    for i in range(1,N):
        if cal(i) == N:
            return i
    return 0

print(sol())