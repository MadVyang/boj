import sys


r, c = map(int, input().split())
bd = []
lu = []
ld = []
ru = []
rd = []
for i in range(r):
    bd.append([int(x) for x in sys.stdin.readline().strip()])
    lu.append([0]*c)
    ld.append([0]*c)
    ru.append([0]*c)
    rd.append([0]*c)

for i in range(r):
    for j in range(c):
        if bd[i][j] == 1:
            if i > 0 and j > 0:
                lu[i][j] = lu[i-1][j-1]+1
            else:
                lu[i][j] = 1
for i in range(r):
    i = r-i-1
    for j in range(c):
        if bd[i][j] == 1:
            if i < r-1 and j > 0:
                ld[i][j] = ld[i+1][j-1]+1
            else:
                ld[i][j] = 1
for i in range(r):
    for j in range(c):
        j = c-j-1
        if bd[i][j] == 1:
            if i > 0 and j < c-1:
                ru[i][j] = ru[i-1][j+1]+1
            else:
                ru[i][j] = 1
for i in range(r):
    i = r-i-1
    for j in range(c):
        j = c-j-1
        if bd[i][j] == 1:
            if i < r-1 and j < c-1:
                rd[i][j] = rd[i+1][j+1]+1
            else:
                rd[i][j] = 1


ans = 0
for i in range(r):
    for j in range(c):
        if bd[i][j] == 1:
            size = min(ld[i][j], rd[i][j])
            for k in range(1, size+1):
                ii = i+2*(k-1)
                if ii < r and min(lu[ii][j], ru[ii][j]) >= k:
                    ans = max(ans, k)
            size = min(ru[i][j], rd[i][j])
            for k in range(1, size+1):
                jj = j+2*(k-1)
                if jj < c and min(lu[i][jj], ld[i][jj]) >= k:
                    ans = max(ans, k)
print(ans)
# print(lu, ld, ru, rd)
