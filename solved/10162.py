t = int(input())
if t % 10 > 0:
    print(-1)
else:
    a, b, c = 0, 0, 0
    if t >= 300:
        a = t//300
        t %= 300
    if t >= 60:
        b = t//60
        t %= 60
    if t >= 10:
        c = t//10
    print(a, b, c)
