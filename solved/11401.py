n, k = [int(x) for x in input().split()]
m = 1000000007

nf = 1
kf = 1
nkf = 1
for i in range(2, n+1):
    nf = (nf*i) % m
for i in range(2, k+1):
    kf = (kf*i) % m
for i in range(2, n-k+1):
    nkf = (nkf*i) % m

t = (kf*nkf) % m
# print(nf, kf, nkf)


def power(x, n):
    # print(x, n)
    if n == 1:
        return x
    if n == 2:
        return x*x
    h = power(x, n//2)
    if n % 2 == 0:
        return (h*h) % m
    else:
        return (h*h*x) % m


t_inv = power(t, m-2)
print((nf*t_inv) % m)
