from itertools import permutations


n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()

check = set()
for p in permutations(arr, m):
    s = ' '.join([str(x) for x in p])
    if s in check:
        continue
    check.add(s)
    print(s)
