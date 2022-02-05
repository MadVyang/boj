n = int(input())
arr = [int(x) for x in input().split()]
m = int(input())

arr.sort(reverse=True)
sum = 0
for i in arr:
    sum+=i
# print(m,sum,arr)
solved=False
if sum<=m:
    print(arr[0])
    solved=True
else:
    sum2 = sum
    for i in range(n-1):
        sum2-=arr[i]
        r = (m-sum2)//(i+1)
        if r>=arr[i+1]:
            print(r)
            solved=True
            break 

if not solved:
    print(m//n)
