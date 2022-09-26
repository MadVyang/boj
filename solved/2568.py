import sys


n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip().split()])
arr.sort()

lis = [arr[0][1]]
idx = [0]

for j, i in arr[1:]:
    if i > lis[-1]:
        lis.append(i)
        idx.append(len(lis)-1)
        continue
    low, high = 0, len(lis)-1
    while low < high:
        mid = low+high
        mid //= 2
        if lis[mid] < i:
            low = mid+1
        else:
            high = mid
    lis[high] = i
    idx.append(high)

# print(idx)
r = []
cur = len(lis)-1
for i in range(n-1, -1, -1):
    if idx[i] == cur:
        r.append(arr[i][0])
        cur -= 1

r = list(set([x[0] for x in arr])-set(r))
print(len(r))
r.sort()
for i in r:
    print(i)
