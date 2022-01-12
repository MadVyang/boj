p, k = [int(x) for x in input().split()]
is_prime = [True]*1000001
primes = []

for i in range(2, 1000001):
    if is_prime[i]:
        primes.append(i)
    for j in range(i*2, 1000001, i):
        is_prime[j] = False
# print(primes)
good = True
for i in primes:
    if i >= k:
        break
    if p % i == 0:
        good = False
        print('BAD', i)
        break
if good:
    print('GOOD')
