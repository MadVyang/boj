ans = 0
s = 0
for i in range(4):
    a, b = map(int, input().split())
    s -= a
    ans = max(ans, s)
    s += b
    ans = max(ans, s)
print(ans)
