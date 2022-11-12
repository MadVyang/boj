n, m = map(int, input().split())
bd = []
for i in range(n):
    bd.append([int(x) for x in input()])

xmx = []
ymx = []
mx = []
for i in range(n):
    xmx.append([0]*m)
    ymx.append([0]*m)
    mx.append([0]*m)
sqs = [[], []]
ans = 0
for i in range(n):
    for j in range(m):
        if bd[i][j] == 1:
            sqs[1].append((i, j))
            xmx[i][j] = 1
            ymx[i][j] = 1
            mx[i][j] = 1
            ans = 1

for i in range(n):
    for j in range(m-2, -1, -1):
        if bd[i][j] == 1:
            xmx[i][j] = xmx[i][j+1]+1
for i in range(n-2, -1, -1):
    for j in range(m):
        if bd[i][j] == 1:
            ymx[i][j] = ymx[i+1][j]+1


for i in range(n-2, -1, -1):
    for j in range(m-2, -1, -1):
        before_size = mx[i+1][j+1]
        if xmx[i][j] >= before_size+1 and ymx[i][j] >= before_size+1:
            mx[i][j] = before_size+1
        elif before_size+1 >= xmx[i][j] or before_size+1 >= ymx[i][j]:
            mx[i][j] = min(xmx[i][j], ymx[i][j])
        ans = max(ans, mx[i][j])

print(ans*ans)
# for i in range(2, 1001):
#     if not sqs[i-1]:
#         break
#     sqs.append([])
#     for y, x in sqs[i-1]:
#         if y+i > n or x+i > m:
#             continue
#         if xmx[y+i-1][x] >= i and ymx[y][x+i-1] >= i:
#             sqs[i].append((y, x))
#     if not sqs[i]:
#         sqs.pop()
#         break
# sqs[i-1].clear()

# for i in range(len(sqs)):
#     print(sqs[i])


# size = len(sqs)-1
# print(size*size)
