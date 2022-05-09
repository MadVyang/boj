import sys


n = int(sys.stdin.readline().strip())
ps, ms = [], []
zero = False
for i in range(n):
    k = int(sys.stdin.readline().strip())
    if k > 0:
        ps.append(k)
    elif k < 0:
        ms.append(k)
    else:
        zero = True
ps.sort(reverse=True)
ms.sort()

sum = 0

i = 0
while i < len(ps):
    if i == len(ps)-1:
        sum += ps[i]
        break
    if ps[i] == 1 or ps[i+1] == 1:
        sum += ps[i]
        i += 1
    else:
        sum += ps[i]*ps[i+1]
        i += 2

i = 0
while i < len(ms):
    if i == len(ms)-1:
        if not zero:
            sum += ms[i]
        break
    sum += ms[i]*ms[i+1]
    i += 2

print(sum)
