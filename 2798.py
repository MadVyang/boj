N, M = map(int,input().split())
arr = list(map(int,input().split()))

max = -1
for i in range(0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            cur = arr[i]+arr[j]+arr[k]
            if cur > max and cur <= M:
                max = cur

print(max)