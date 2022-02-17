n = int(input())
sw = [-1]
sw.extend([int(x) for x in input().split()])
m = int(input())
for _ in range(m):
    s, k = [int(x) for x in input().split()]
    if s == 1:
        for i in range(k, n+1, k):
            sw[i] = 1-sw[i]
    else:
        for i in range(n):
            if k-i < 1 or k+i > n:
                break
            if sw[k-i] != sw[k+i]:
                break
            sw[k-i] = 1-sw[k-i]
            if i > 0:
                sw[k+i] = 1-sw[k+i]

s = ''
for i in range(1, n+1):
    s += str(sw[i])+' '
    if i % 20 == 0:
        print(s)
        s = ''

if len(s) > 0:
    print(s)
