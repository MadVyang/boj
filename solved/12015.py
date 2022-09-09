from bisect import bisect_left


n = int(input())
arr = [int(x) for x in input().split()]

dp = [arr[0]]
for i in range(1, n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        continue

    # left, right = 0, len(dp)
    # while left < right:
    #     mid = (left+right)//2
    #     if dp[mid] < arr[i]:
    #         left = mid+1
    #     else:
    #         right = mid
    dp[bisect_left(dp, arr[i])] = arr[i]

print(len(dp))
