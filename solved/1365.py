n = int(input())
arr = [int(x) for x in input().split()]
lis = [arr[0]]

for i in arr[1:]:
    if i > lis[-1]:
        lis.append(i)
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

# print(lis)
print(n-len(lis))
