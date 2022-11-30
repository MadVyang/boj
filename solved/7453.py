n = int(input())
a, b, c, d = [], [], [], []
for i in range(n):
    q = [int(x) for x in input().split()]
    a.append(q[0])
    b.append(q[1])
    c.append(q[2])
    d.append(q[3])
ab = {}
for i in a:
    for j in b:
        if i+j not in ab:
            ab[i+j] = 0
        ab[i+j] += 1
        # ab.append(i+j)
ans = 0
# cd = []
for i in c:
    for j in d:
        # cd.append(i+j)
        x = i+j
        if -x in ab:
            ans += ab[-x]

print(ans)
