import math

x, y = [int(x) for x in input().split()]
n = y-x
if n == 0:
    print(0)
else:
    k = int(math.sqrt(n))*10

    for i in range(k, -1, -1):
        if (i+1)*(i+1) == n:
            print(i*2+1)
            break
        if (i+1)*(i+1) < n:
            r = (n-(i+1)*(i+1))
            if r == (i+1)*2:
                print(i*2+1+2)
            elif r > (i+1):
                print(i*2+1+2)
            else:
                print(i*2+1+1)
            break
