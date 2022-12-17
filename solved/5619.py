arr = [int(input()) for _ in range(int(input()))]
arr.sort()
arr=arr[:5]
arr2 = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if i!=j:
            arr2.append(int(str(arr[i])+str(arr[j])))
arr2.sort()
print(arr2[2])
            