n = int(input())
arr = [int(x) for x in input().split()]
d = {}
for i in arr:
    if i not in d:
        d[i] = 0
    d[i] += 1
ans = 0
for i in range(n):
    for j in range(n):
        if arr[i]==arr[j] == 0 and d[arr[i]] == 2:
            continue
        if arr[j] == 0 and d[arr[i]] == 1:
            continue
        if i == j:
            continue
        if arr[i]-arr[j] in d:
            if arr[i]-arr[j] == arr[j] and d[arr[j]] == 1:
                continue
            ans += 1
            # print(arr[i], arr[j])
            break
print(ans)
