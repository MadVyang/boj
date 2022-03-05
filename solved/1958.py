a = [x for x in input()]
b = [x for x in input()]
c = [x for x in input()]
a.insert(0, '.')
b.insert(0, '.')
c.insert(0, '.')
la = len(a)
lb = len(b)
lc = len(c)

ans = [[[0]*lc for y in range(lb)] for x in range(la)]
for i in range(la):
    for j in range(lb):
        for k in range(lc):
            if i == 0 or j == 0 or k == 0:
                ans[i][j][k] = 0
            elif a[i] == b[j] == c[k]:
                ans[i][j][k] = ans[i-1][j-1][k-1]+1
            else:
                ans[i][j][k] = max(ans[i-1][j][k], ans[i][j-1][k], ans[i][j][k-1])
print(ans[la-1][lb-1][lc-1])
