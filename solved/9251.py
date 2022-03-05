a = [x for x in input()]
b = [x for x in input()]
a.insert(0, '.')
b.insert(0, '.')
la = len(a)
lb = len(b)

ans = [[0]*(lb) for x in range(la)]
for i in range(la):
    for j in range(lb):
        if i == 0 or j == 0:
            ans[i][j] = 0
        elif a[i] == b[j]:
            ans[i][j] = ans[i-1][j-1]+1
        else:
            ans[i][j] = max(ans[i][j-1], ans[i-1][j])
print(ans[la-1][lb-1])
