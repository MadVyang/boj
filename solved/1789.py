s = int(input())

l = 1
h = s
while l < h:
    m = (l+h)//2
    k = m*(m+1)//2
    if k >= s:
        h = m
        continue
    l = m+1

if h*(h+1)//2 == s:
    print(h)
else:
    print(h-1)
