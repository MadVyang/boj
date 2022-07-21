s, m = 0, 100
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        s += a
        m = min(m, a)
if s == 0:
    print(-1)
else:
    print(s)
    print(m)
