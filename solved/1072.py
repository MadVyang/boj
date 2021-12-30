import math

x, y = [int(x) for x in input().split()]

if x == y or (y*100 // x) == 99:
    print(-1)
elif x < 100:
    z = y*100 // x
    a = 0
    while True:
        a += 1
        if z != (y+a)*100 // (x+a):
            print(a)
            break
else:
    z = y*100 // x
    a = ((z+1)*x-100*y)
    b = 100-(z+1)
    if a % b == 0:
        print(a//b)
    else:
        print(math.ceil(a/b))
