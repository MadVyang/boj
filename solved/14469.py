n = int(input())
arr = [[int(x) for x in input().split()] for _ in range(n)]

t = 0
while len(arr) > 0:
    si = -1
    ct = 123456789
    for i in range(len(arr)):
        if arr[i][0] <= t:
            if arr[i][1] <= ct:
                ct = arr[i][1]
                si = i
    if si != -1:
        t += ct
    else:
        at = 123456789
        for i in range(len(arr)):
            if arr[i][0] <= at:
                at = arr[i][0]
                si = i
        t = arr[si][0]+arr[si][1]

    # print(arr[si])
    arr.pop(si)

print(t)
