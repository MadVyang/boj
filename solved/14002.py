n=int(input())
arr=[int(x) for x in input().split()]
dp = []
for i in range(n):
    dp.append([arr[i]])
    for j in range(i):
        if arr[i]>arr[j] and len(dp[i])<=len(dp[j]):
            dp[i]=dp[j]+[arr[i]]

ans = []
for i in range(n):
    if len(ans)<len(dp[i]):
        ans = dp[i]
print(len(ans))
print(' '.join([str(x) for x in ans]))