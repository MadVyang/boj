n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
l = 0
h = max(arr)+1
while l < h:
    mid = (l+h)//2
    sum = 0
    for i in arr:
        sum += max(i-mid, 0)
    if sum < m:
        h = mid
    else:
        l = mid+1
print(l-1)
