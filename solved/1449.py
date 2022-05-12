n, l = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()

cur = arr[0]
ans = 0

i = 1
while i <= n-1:
    if arr[i]-cur >= l:
        ans += 1
        cur = arr[i]
    i += 1

print(ans+1)
