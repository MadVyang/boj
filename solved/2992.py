from itertools import permutations

arr = [int(x) for x in input()]
p = sorted(list(permutations(arr, len(arr))))
try:
    idx = p.index(tuple(i for i in arr))+1
    while p[idx] == tuple(i for i in arr):
        idx += 1
    print(''.join([str(i) for i in p[idx]]))
except:
    print(0)
