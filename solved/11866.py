n, k = [int(x) for x in input().split()]
i = -1
arr = [i+1 for i in range(n)]
r = []
while arr:
    for _ in range(k):
        i += 1
        if i == len(arr):
            i %= len(arr)
    r.append(str(arr[i]))
    arr.pop(i)
    i -= 1
print('<'+', '.join(r)+'>')
