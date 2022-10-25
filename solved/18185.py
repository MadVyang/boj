n = int(input())
arr = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    while arr[i]:
        if ((i < n-2 and arr[i] > 0 and arr[i+1] > 0 and arr[i+2] > 0)
                and (arr[i+1] <= arr[i+2])):
            ans += 7
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
        elif i < n-1 and arr[i] > 0 and arr[i+1] > 0:
            ans += 5
            arr[i] -= 1
            arr[i+1] -= 1
        else:
            ans += 3*arr[i]
            arr[i] = 0
        # print(arr, ans)
print(ans)
