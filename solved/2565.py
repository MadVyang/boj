n=int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])
arr.sort()

length = [1]*n

for i in range(n):
    for j in range(i):
        if arr[i][1]>arr[j][1]:
            length[i]=max(length[i],length[j]+1)

print(n-max(length))