a,b=[int(x) for x in input().split()]
c,d=[int(x) for x in input().split()]
e,f=[int(x) for x in input().split()]

v1 = (c-a, d-b)
v2 = (e-c, f-d)

m = v1[0]*v2[1]-v1[1]*v2[0]
if m>0:
    print(1)
if m<0:
    print(-1)
if m==0:
    print(0)