import itertools
import math


n, d = [int(x) for x in input().split()]

nums = [i for i in range(d)]
pm = itertools.permutations(nums)
mn = math.inf
for p in pm:
    if p[d-1] == 0:
        continue
    r = 0
    for i in range(d):
        r += p[i]*(d**i)
    if r > n:
        mn = min(mn, r)
if mn == math.inf:
    mn = -1
print(mn)
