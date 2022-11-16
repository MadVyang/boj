n, m = map(int, input().split())
ans = 0
for i in range(n):
    s = set()
    for c in input():
        if ord(c)-ord('A')+1 > m:
            break
        if c in s:
            break
        s.add(c)
    else:
        ans += 1
print(ans)
