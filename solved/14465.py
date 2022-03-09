n, k, b = [int(x) for x in input().split()]
arr = [False]*(n+1)
for _ in range(b):
    arr[int(input())] = True

count = 0
for i in range(1, k+1):
    if arr[i]:
        count += 1

mn = count
for i in range(k+1, n+1):
    if arr[i]:
        count += 1
    if arr[i-k]:
        count -= 1
    if count < mn:
        mn = count
    # print(i-k,i,count)
print(mn)
