import sys


n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for x in range(n)]
arr.sort()

ans = 0
ans = max(ans, abs(arr[0]+arr[-1]-arr[1]*2))
ans = max(ans, abs(arr[0]+arr[-1]-arr[-2]*2))
ans = max(ans, abs(arr[-3]+arr[-1]-arr[-2]*2))
for i in range(1,n-1):
    ans = max(ans, abs(arr[i-1]+arr[i+1]-arr[i]*2))
    ans = max(ans, abs(arr[0]+arr[-1]-arr[i]*2))
    ans = max(ans, abs(arr[0]+arr[i+1]-arr[i]*2))
    ans = max(ans, abs(arr[i-1]+arr[-1]-arr[i]*2))
    

print(ans)
