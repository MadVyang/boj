arr = [[int(x) for x in input().split()] for i in range(9)]
max = arr[0][0]
si,sj=0,0
for i in range(9):
    for j in range(9):
        if arr[i][j]>max:
            max=arr[i][j]
            si,sj=i,j
print(max)
print(si+1,sj+1)