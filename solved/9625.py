k=int(input())
a=[1]+[0]*k
b = [0]+[0]*k
for i in range(1,k+1):
    a[i]=b[i-1]
    b[i]=a[i-1]+b[i-1]
print(a[k],b[k])