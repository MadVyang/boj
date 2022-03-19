n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

current = 0
ans = 0
for i in range(n):
    if arr[i] > current+1:
        ans =current+1
        break
    else:
        current += arr[i]
if ans==0:
    ans = sum(arr)+1
print(ans)