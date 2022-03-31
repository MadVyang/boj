n = int(input())
mx = 0
for _ in range(n):
    a, b, c = [int(x) for x in input().split()]
    if a == b == c:
        mx = max(mx, a*1000+10000)
    elif a == b:
        mx = max(mx, a*100+1000)
    elif a == c:
        mx = max(mx, a*100+1000)
    elif c == b:
        mx = max(mx, c*100+1000)
    else:
        mx = max(mx, max(a, b, c)*100)
print(mx)
