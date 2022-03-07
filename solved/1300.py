n = int(input())
k = int(input())

# a = [[i*j for j in range(n+1)] for i in range(n+1)]
# for i in range(1, n+1):
#     print(a[i][1:])

left = 1
right = n*n
mid = 1
while left <= right:
    mid = (left+right)//2
    count = 0
    for i in range(1, n+1):
        count += min(mid//i, n)
    if count < k:
        left = mid+1
    else:
        right = mid-1
print(left)
