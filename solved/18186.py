n, b, c = map(int, input().split())
arr = [int(x) for x in input().split()]

if b <= c:
    print(sum(arr)*b)
    exit()

ans = 0
for i in range(n):
    while arr[i]:
        if ((i < n-2 and arr[i] > 0 and arr[i+1] > 0 and arr[i+2] > 0)
                and (arr[i+1] <= arr[i+2])):
            buy = min(arr[i], arr[i+1], arr[i+2])
            ans += (b+c*2)*buy
            arr[i] -= buy
            arr[i+1] -= buy
            arr[i+2] -= buy
        elif i < n-1 and arr[i] > 0 and arr[i+1] > 0:
            buy = min(arr[i], arr[i+1])
            if i < n-2 and arr[i+1] > arr[i+2]:
                buy = min(buy, arr[i+1]-arr[i+2])
            ans += (b+c)*buy
            arr[i] -= buy
            arr[i+1] -= buy
        else:
            ans += b*arr[i]
            arr[i] = 0
        # print(arr, ans)
print(ans)
