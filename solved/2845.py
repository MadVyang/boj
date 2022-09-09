l,p = map(int,input().split())
arr = [int(x) for x in input().split()]
s = ''
for i in arr:
    s+=str(-l*p+i)+' '
print(s)