n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
# print(arr)
for i in range(n-1):
    arr[i+1] += arr[i]

# print(arr)
sum = 0
for i in range(n):
    sum += arr[i]
print(sum)
