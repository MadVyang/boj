n = int(input())
arr = [int(x) for x in input().split()]
s = set(arr)
check = set()
x = int(input())

ans = 0
for i in range(n):
    if arr[i] in check:
        continue
    if x-arr[i] != arr[i] and x-arr[i] in s and x-arr[i] not in check:
        check.add(arr[i])
        check.add(x-arr[i])
        ans += 1
        # print(arr[i])
print(ans)
