n = int(input())
arr = [int(x) for x in input().split()]

ans = 0


def merge(s, e):
    global ans
    m = (s+e)//2
    result = []
    i, j = s, m+1
    while i <= m or j <= e:
        if i > m:
            result.append(arr[j])
            j += 1
        elif j > e:
            result.append(arr[i])
            i += 1
        elif arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1
            ans += m+1-i
    for i in range(len(result)):
        arr[i+s] = result[i]


def merge_sort(s, e):
    if s == e:
        return
    m = (s+e)//2
    merge_sort(s, m)
    merge_sort(m+1, e)
    merge(s, e)


merge_sort(0, n-1)
print(ans)


# print(arr)
