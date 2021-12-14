N = int(input())
pan = []
ans = []
for i in range(N):
    pan.append(list(map(int,input().split())))
    ans.append([0]*N)
ans[0][0] = 1

for i in range(N):
    for j in range(N):
        if i==N-1 and j==N-1:
            continue
        value = pan[i][j]
        if i+value<N:
            ans[i+value][j]+=ans[i][j]
        if j+value<N:
            ans[i][j+value]+=ans[i][j]

print(ans[N-1][N-1])