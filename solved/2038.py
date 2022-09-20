n = int(input())
arr = [0]*11111111
arr[1] = 1
cur = 1
sum = 1
while sum < n:
    cur += 1
    arr[cur] = 1+arr[cur-arr[arr[cur-1]]]
    sum += arr[cur]

print(cur)
