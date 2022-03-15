import sys

k, n = [int(x) for x in input().split()]
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline().strip()))


def count(l):
    result = 0
    for i in range(k):
        result += arr[i]//l
    return result


left = 1
right = max(arr)+1
while left < right:
    mid = (left+right)//2
    if count(mid) < n:
        right = mid
    else:
        left = mid+1

print(right-1)
