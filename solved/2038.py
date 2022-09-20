n = int(input())
arr = [0, 1, 2, 2]
cur = 2
sum = 3
while sum < n:
    cur += 1
    if len(arr) <= 11111111:
        arr += [cur]*arr[cur]
    sum += arr[cur]
if n == 1:
    cur = 1
print(cur)
