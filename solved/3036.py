n= int(input())
arr=[int(x) for x in input().split()]

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

for i in range(1,n):
    g = gcd(arr[0],arr[i])
    print(str(arr[0]//g)+'/'+str(arr[i]//g))