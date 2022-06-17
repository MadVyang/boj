n = int(input())
arr = []
_n = n

for i in range(2, n+1):
    if i*i > n:
        break
    if _n % i == 0:
        arr.append(i)
        while _n % i == 0:
            _n //= i

if _n != 1:
    arr.append(_n)
# print(arr)


s = set()
for i in arr:
    n //= i
    n *= i-1
print(n)
