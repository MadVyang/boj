n = int(input())
al = [int(x) for x in input().split()]
b, c = [int(x) for x in input().split()]

ans = n
for a in al:
    if b >= a:
        continue
    if (a-b) % c == 0:
        ans += (a-b)//c
    else:
        ans += (a-b)//c+1

print(ans)
